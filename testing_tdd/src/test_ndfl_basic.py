from ndfl import calculation_tax

def test_basic_ndfl():
    assert calculation_tax(200_000) == 26_000


def test_ndfl_tier_2():
    assert calculation_tax(300_000) == 402_000

def test_ndfl_tier_3():
    assert calculation_tax(7_000_000_000) == 1_062_000

def test_ndfl_tier_4():
    assert calculation_tax(30_000_000_000) == 5_402_000

def test_ndfl_tier_5():
    assert calculation_tax(70_000_000_000) == 13_802_000


