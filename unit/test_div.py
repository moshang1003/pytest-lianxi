from unit.div import div


def test_div_int():
    assert div(10, 2) == 5
    assert div(10, 5) == 2
    assert div(100000000, 1) == 100000000


def test_div_float():
    assert div(10, 3) == 3.333333333333333
    assert div(10.2, 0.2) == 51


def test_div_expection():
    assert div(10, 'a')
    assert div('abc', 10)


def test_div_zero():
    assert div(10, 0) == None


def test_div_fushu():
    assert div(-10, 2) == -5
    assert div(-10, -2) == 5




