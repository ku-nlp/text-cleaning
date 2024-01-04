from jp_broom.helpers import (clean_brackets, clean_commas,
                              clean_double_hyphens, clean_ellipses, clean_full_stops, clean_wave_dash)


def test_clean_brackets():
    # Test standardization
    assert clean_brackets("「") == "「"
    assert clean_brackets("『") == "「"
    assert clean_brackets("（") == "「"
    assert clean_brackets("〔") == "「"
    assert clean_brackets("［") == "「"
    assert clean_brackets("｛") == "「"
    assert clean_brackets("｟") == "「"
    assert clean_brackets("〈") == "「"
    assert clean_brackets("《") == "「"
    assert clean_brackets("【") == "「"
    assert clean_brackets("〖") == "「"
    assert clean_brackets("〘") == "「"
    assert clean_brackets("〚") == "「"
    assert clean_brackets("＜") == "「"
    assert clean_brackets("」") == "」"
    assert clean_brackets("』") == "」"
    assert clean_brackets("）") == "」"
    assert clean_brackets("〕") == "」"
    assert clean_brackets("］") == "」"
    assert clean_brackets("｝") == "」"
    assert clean_brackets("｠") == "」"
    assert clean_brackets("〉") == "」"
    assert clean_brackets("》") == "」"
    assert clean_brackets("】") == "」"
    assert clean_brackets("〗") == "」"
    assert clean_brackets("〙") == "」"
    assert clean_brackets("〛") == "」"
    assert clean_brackets("＞") == "」"

    # Test removal
    assert clean_brackets("「", remove=True) == ""
    assert clean_brackets("『", remove=True) == ""
    assert clean_brackets("（", remove=True) == ""
    assert clean_brackets("〔", remove=True) == ""
    assert clean_brackets("［", remove=True) == ""
    assert clean_brackets("｛", remove=True) == ""
    assert clean_brackets("｟", remove=True) == ""
    assert clean_brackets("〈", remove=True) == ""
    assert clean_brackets("《", remove=True) == ""
    assert clean_brackets("【", remove=True) == ""
    assert clean_brackets("〖", remove=True) == ""
    assert clean_brackets("〘", remove=True) == ""
    assert clean_brackets("〚", remove=True) == ""
    assert clean_brackets("＜", remove=True) == ""
    assert clean_brackets("」", remove=True) == ""
    assert clean_brackets("』", remove=True) == ""
    assert clean_brackets("）", remove=True) == ""
    assert clean_brackets("〕", remove=True) == ""
    assert clean_brackets("］", remove=True) == ""
    assert clean_brackets("｝", remove=True) == ""
    assert clean_brackets("｠", remove=True) == ""
    assert clean_brackets("〉", remove=True) == ""
    assert clean_brackets("》", remove=True) == ""
    assert clean_brackets("】", remove=True) == ""
    assert clean_brackets("〗", remove=True) == ""
    assert clean_brackets("〙", remove=True) == ""
    assert clean_brackets("〛", remove=True) == ""
    assert clean_brackets("＞", remove=True) == ""


def test_clean_commas():
    # Test standardization
    assert clean_commas("、") == "、"
    assert clean_commas("，") == "、"
    assert clean_commas("﹐") == "、"

    # Test removal
    assert clean_commas("、", remove=True) == ""
    assert clean_commas("，", remove=True) == ""
    assert clean_commas("﹐", remove=True) == ""

    # Test conversion
    assert clean_commas("、", convert=True) == " "
    assert clean_commas("，", convert=True) == " "
    assert clean_commas("﹐", convert=True) == " "


def test_clean_double_hyphens():
    # Test standardization
    assert clean_double_hyphens("゠") == "＝"
    assert clean_double_hyphens("＝") == "＝"

    # Test removal
    assert clean_double_hyphens("゠", remove=True) == ""
    assert clean_double_hyphens("＝", remove=True) == ""


def test_clean_ellipses():
    # Test standardization
    assert clean_ellipses("…") == "…"
    assert clean_ellipses("‥") == "…"
    assert clean_ellipses("・") == "…"

    # Test removal
    assert clean_ellipses("…", remove=True) == ""
    assert clean_ellipses("‥", remove=True) == ""
    assert clean_ellipses("・", remove=True) == ""


def test_clean_full_stops():
    # Test standardization
    assert clean_full_stops("。") == "。"
    assert clean_full_stops("．") == "。"
    assert clean_full_stops(".") == "。"

    # Test removal
    assert clean_full_stops("。", remove=True) == ""
    assert clean_full_stops("．", remove=True) == ""
    assert clean_full_stops(".", remove=True) == ""

    # Test conversion
    assert clean_full_stops("。", convert=True) == " "
    assert clean_full_stops("．", convert=True) == " "
    assert clean_full_stops(".", convert=True) == " "


def test_clean_wave_dash():
    # Test standardization
    assert clean_wave_dash("〜") == "〜"
    assert clean_wave_dash("～") == "〜"

    # Test removal
    assert clean_wave_dash("〜", remove=True) == ""
    assert clean_wave_dash("～", remove=True) == ""
