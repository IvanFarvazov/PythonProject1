import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number('2202345612340099') == '2202 34** **** 0099'

def test_get_mask_account():
    assert get_mask_account('22023456123400991234') == '**1234'