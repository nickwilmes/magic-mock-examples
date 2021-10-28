from typing import Any
from unittest.mock import MagicMock, patch
import pytest


class Exception1(Exception):
    pass


class Exception2(Exception):
    pass


def foo() -> Any:
    try:
        return bar(1, 2)+bar(3, 4)
    except Exception1:
        return 0


def bar(a: Any, b: Any) -> Any:
    return 1


@patch(f"{__name__}.bar")
def test_foo__raise_exception(bar_mock: MagicMock):
    bar_mock.side_effect = Exception1

    result = foo()

    assert bar_mock.call_count == 1
    assert result == 0


@patch(f"{__name__}.bar")
def test_foo__raise_exception_second_time(bar_mock: MagicMock):
    bar_mock.side_effect = [1, Exception1]

    result = foo()

    assert bar_mock.call_count == 2
    assert result == 0


@patch(f"{__name__}.bar")
def test_foo__catch_raised_exception(bar_mock: MagicMock):
    bar_mock.side_effect = Exception2

    with pytest.raises(Exception2):
        foo()