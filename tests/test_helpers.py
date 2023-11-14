from jp_broom.helpers import (standardize_brackets, standardize_commas,
                              standardize_double_hyphens, standardize_ellipses, standardize_full_stops, standardize_wave_dash)


def test_standardize_brackets():
    assert standardize_brackets("「") == "「"
    assert standardize_brackets("『") == "「"
    assert standardize_brackets("（") == "「"
    assert standardize_brackets("〔") == "「"
    assert standardize_brackets("［") == "「"
    assert standardize_brackets("｛") == "「"
    assert standardize_brackets("｟") == "「"
    assert standardize_brackets("〈") == "「"
    assert standardize_brackets("《") == "「"
    assert standardize_brackets("【") == "「"
    assert standardize_brackets("〖") == "「"
    assert standardize_brackets("〘") == "「"
    assert standardize_brackets("〚") == "「"
    assert standardize_brackets("＜") == "「"
    assert standardize_brackets("」") == "」"
    assert standardize_brackets("』") == "」"
    assert standardize_brackets("）") == "」"
    assert standardize_brackets("〕") == "」"
    assert standardize_brackets("］") == "」"
    assert standardize_brackets("｝") == "」"
    assert standardize_brackets("｠") == "」"
    assert standardize_brackets("〉") == "」"
    assert standardize_brackets("》") == "」"
    assert standardize_brackets("】") == "」"
    assert standardize_brackets("〗") == "」"
    assert standardize_brackets("〙") == "」"
    assert standardize_brackets("〛") == "」"
    assert standardize_brackets("＞") == "」"


def test_standardize_commans():
    assert standardize_commas("、") == "、"
    assert standardize_commas("，") == "、"
    assert standardize_commas("﹐") == "、"


def test_standardize_double_hyphens():
    assert standardize_double_hyphens("゠") == "＝"
    assert standardize_double_hyphens("＝") == "＝"


def test_standardize_ellipses():
    assert standardize_ellipses("…") == "…"
    assert standardize_ellipses("‥") == "…"


def test_standardize_full_stops():
    assert standardize_full_stops("。") == "。"
    assert standardize_full_stops("．") == "。"
    assert standardize_full_stops(".") == "。"


def test_standardize_wave_dash():
    assert standardize_wave_dash("〜") == "〜"
    assert standardize_wave_dash("～") == "〜"