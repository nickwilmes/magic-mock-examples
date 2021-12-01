def third_party_method() -> int:
    pass


def foo(a: int, b: int):
    if a > third_party_method():
        return b
    else:
        return 2 * b


def test_foo__a_less_than_third_party_method():
    """Attempt to test what will happen if a is less than what the third party method returns"""
    assert False


def test_foo__a_greater_than_third_party_method():
    """Attempt to test what will happen if a is greater than what the third party method returns"""
    assert False


def test_foo__a_equals_than_third_party_method():
    """Attempt to test what will happen if a is equal to what the third party method returns"""
    assert False
