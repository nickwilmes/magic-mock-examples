def third_party_method(amount: int) -> int:
    pass


def foo() -> int:
    try:
        third_party_method(10)
    except Exception:
        return 0

    try:
        return third_party_method(20)
    except Exception:
        return -1


def test_foo__third_party_method_thorws_exception():
    """
    Attempt to verify that when third_party_method throws an Exception,
    foo will return 0
    """
    assert False


def test_foo__third_party_method_thorws_exception_on_second_call():
    """
    Attempt to verify that when third_party_method throws an Exception
    on the second call, foo will return -1
    """
    assert False
