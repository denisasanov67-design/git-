 from ndfl import calculation_tax

def test_basic_ndfl():
    assert calculation_tax(200_000) == 260_000