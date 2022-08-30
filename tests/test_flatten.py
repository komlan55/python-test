import pytest

from modules.flatten import flattenList


@pytest.mark.parametrize(
    "nested_list, expected",
    [
        ([['1', 2, [3]], 4], ['1', 2, 3, 4]),
        (['1', 2, 3, [4], [], [[[[[[[[[5]]]]]]]]]], ['1', 2, 3, 4, 5])
    ]
)
def test_flatten_list(nested_list, expected):
    assert expected == flattenList(nested_list)
