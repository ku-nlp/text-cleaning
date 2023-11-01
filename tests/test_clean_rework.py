from jp_broom import normalize_width


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

