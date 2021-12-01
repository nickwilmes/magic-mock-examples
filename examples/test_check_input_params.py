from typing import Any
from unittest.mock import MagicMock, patch


def foo(a: Any, b: Any) -> Any:
    return bar(a, b)


def bar(a: Any, b: Any) -> Any:
    return a + b


@patch(f"{__name__}.bar")
def test_foo__exact_parameter_validation(bar_mock: MagicMock):
    bar_mock.return_value = 2

    a, b = (1, 2)
    result = foo(a, b)

    bar_mock.assert_called_once_with(a, b)
    assert result == 2


@patch(f"{__name__}.bar")
def test_foo__partial_parameter_validation(bar_mock: MagicMock):
    bar_mock.return_value = "12"

    a, b = "1", "2"
    result = foo(a, b)

    bar_mock.assert_called_once()

    called_args = bar_mock.call_args.args
    assert type(called_args[0]) == str
    assert len(called_args[1]) == 1
    assert result == "12"
