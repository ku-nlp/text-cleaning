from jp_broom.helpers import (normalize_width, clean_whitespace, clean_laughter,
                              clean_repeating_characters, clean_kaomoji, clean_numbers)


def test_normalize_width():
    """Test normalize_width function"""
    assert normalize_width("ｱｲｳｴｵ") == "アイウエオ"
    assert normalize_width("ｶﾞｷﾞｸﾞｹﾞｺﾞ") == "ガギグゲゴ"
    assert normalize_width("ｻﾞｼﾞｽﾞｾﾞｿﾞ") == "ザジズゼゾ"
    assert normalize_width("ﾀﾞﾁﾞﾂﾞﾃﾞﾄﾞ") == "ダヂヅデド"
    assert normalize_width("ﾊﾞﾋﾞﾌﾞﾍﾞﾎﾞ") == "バビブベボ"
    assert normalize_width("ﾊﾟﾋﾟﾌﾟﾍﾟﾎﾟ") == "パピプペポ"
    assert normalize_width("ｬｭｮ") == "ャュョ"
    assert normalize_width("ｯ") == "ッ"
    assert normalize_width("ｰ") == "ー"
    assert normalize_width("｡") == "。"
    assert normalize_width("｢") == "「"
    assert normalize_width("｣") == "」"
    assert normalize_width("､") == "、"
    assert normalize_width("･") == "・"
    assert normalize_width("､") == "、"
    assert normalize_width("･") == "・"


def test_clean_whitespace():
    """Test clean_whitespace function"""
    # Test with default parameters (convert=True, remove=False)
    assert clean_whitespace("  あいうえお  ") == " あいうえお "

    # Test with remove=True
    assert clean_whitespace("  あいうえお  ", remove=True) == "あいうえお"

    # Test with convert=False, remove=False
    assert clean_whitespace("  あいうえお  ", convert=False) == " あいうえお "
    assert clean_whitespace("あい  うえ  お", convert=False) == "あい うえ お"

    # Test with convert=False, remove=True
    assert clean_whitespace("あい  うえ  お", remove=True, convert=False) == "あいうえお"


def test_clean_laughter():
    """Test clean_laughter function"""
    assert clean_laughter("笑笑笑") == "笑"
    assert clean_laughter("笑笑笑", remove=True) == ""
    assert clean_laughter("wwww") == "w"
    assert clean_laughter("wwww", remove=True) == ""


def test_clean_repeating_characters():
    """Test clean_repeating_characters function"""
    assert clean_repeating_characters("あああああ") == "あ"
    assert clean_repeating_characters("ああ", min_repeats=3) == "ああ"
    assert clean_repeating_characters("あああああ", remove=True) == ""


def test_clean_kaomoji():
    """Test clean_kaomoji function"""
    assert clean_kaomoji("(°◡°♡)") == ""
    assert clean_kaomoji("(─‿‿─)") == ""
    assert clean_kaomoji("(´・ω・`)") == ""
    assert clean_kaomoji("(^◡^)( ´∀` )") == ""

    # make sure it doesn't remove normal full stops
    assert clean_kaomoji("あああ。") == "あああ。"


def test_clean_numbers():
    """Test clean_numbers function"""

    # Test for removing numbers
    assert clean_numbers("テスト123テスト", remove=True) == "テストテスト"
    assert clean_numbers("テスト０１２テスト", remove=True) == "テストテスト"

    # Test for converting full-width to half-width
    assert clean_numbers("テスト０１２テスト", convert=True) == "テスト012テスト"
    assert clean_numbers("テスト４５６テスト", convert=True) == "テスト456テスト"

    # Test for no action (neither remove nor convert)
    assert clean_numbers("テストテスト") == "テストテスト"
    assert clean_numbers("テスト123テスト") == "テスト123テスト"
    assert clean_numbers("テスト０１２テスト") == "テスト０１２テスト"

    # Ensure it doesn't convert half-width to full-width when convert=False
    assert clean_numbers("テスト123テスト", convert=False) == "テスト123テスト"
