def third_party_method(amount: int) -> int:
    pass


def foo(a: int, b: int) -> int:
    if a > b:
        return third_party_method(a) - third_party_method(b)
    else:
        return third_party_method(a) + third_party_method(b) + third_party_method(a + b)


def test_foo__a_greater_than_b():
    """
    Attempt to verify that when a is greater than b, third_party_method is
    called twice, once with a and once with b
    """
    assert False


def test_foo__b_greater_than_a():
    """
    Attempt to verify that when b is greater than a, third_party_method is
    called 3 times.  First with a, second with b and third with a+b
    """
    assert False
