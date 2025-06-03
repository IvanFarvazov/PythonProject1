import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "data, result",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("64686473678894779589", "Введен неверный номер карты"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("35383033474447895560", "Введен неверный номер карты"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
        ("73654108430135874305", "Введен неверный номер карты"),
    ],
)
def test_get_mask_card_number(data, result):
    assert get_mask_card_number(data) == result


@pytest.mark.parametrize(
    "data, result",
    [("64686473678894779589", "**9589"), ("35383033474447895560", "**5560"), ("73654108430135874305", "**4305")],
)
def test_get_mask_account(data, result):
    assert get_mask_account(data) == result
