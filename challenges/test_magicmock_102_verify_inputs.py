from random import randrange


def third_party_method(amount: int) -> int:
    pass


def third_party_method2(amount: int, more_input: object) -> int:
    pass


def foo(a: int, b: int) -> int:
    third_party_response = third_party_method(b)
    if a > third_party_response:
        return b
    else:
        return 2 * b


def bar(a: int, b: int) -> int:
    third_party_response = third_party_method(a + b)
    if a > third_party_response:
        return third_party_method2(b, randrange(10))
    else:
        return 2 * b


def test_foo__verify_b_is_passed_to_third_party_method():
    """
    Attempt to test that foo is passing your second input to third_party_method
    """
    assert False


def test_bar__verify_2b_is_passed_to_third_party_method():
    """
    Attempt to test that bar is doubling your second input and then passing it
    to third_party_method
    """
    assert False


def test_bar__verify_third_party_method2_inputs():
    """
    Attempt to test that when bar is called and a is less than the response
    from third_party_method, third_party_method2 is called with a specific
    input for the first parameter and an int from 0-9 for the second
    parameter
    """
    assert False
