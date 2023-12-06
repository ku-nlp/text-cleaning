from jp_broom.helpers import (normalize_width, clean_whitespace, clean_laughter, clean_repeating_characters, clean_kaomoji)


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
    assert clean_whitespace("  あいうえお  ") == " あいうえお "
    assert clean_whitespace("  あいうえお  ", remove=True) == "あいうえお"


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
