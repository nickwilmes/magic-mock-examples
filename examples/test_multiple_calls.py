from typing import Any
from unittest.mock import MagicMock, patch


def foo() -> Any:
    sum = 0
    for i in range(3):
        sum += bar(i, i + 1)
    return sum


def bar(a: Any, b: Any) -> Any:
    return 0


@patch(f"{__name__}.bar")
def test_foo__verify_multiple_calls(bar_mock: MagicMock):
    bar_mock.return_value = 1

    result = foo()

    assert bar_mock.call_count == 3
    assert bar_mock.call_args_list[0].args == (0, 1)
    assert bar_mock.call_args_list[1].args == (1, 2)
    assert bar_mock.call_args_list[2].args == (2, 3)


@patch(f"{__name__}.bar")
def test_foo__provide_different_responses_for_mock(bar_mock: MagicMock):
    bar_mock.side_effect = [1, 2, 3]

    result = foo()

    assert result == 6
