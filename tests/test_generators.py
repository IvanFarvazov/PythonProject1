from typing import Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


class TestFilterByCurrency:
    def test_filter_usd(self, sample_transactions):
        result = list(filter_by_currency(sample_transactions, "USD"))
        assert len(result) == 2
        assert all(t["currency"] == "USD" for t in result)

    def test_filter_eur(self, sample_transactions):
        result = list(filter_by_currency(sample_transactions, "EUR"))
        assert len(result) == 1
        assert result[0]["currency"] == "EUR"

    def test_filter_empty_result(self, sample_transactions):
        result = list(filter_by_currency(sample_transactions, "JPY"))
        assert len(result) == 0


class TestTransactionDescriptions:
    def test_descriptions_order(self, sample_transactions):
        gen = transaction_descriptions(sample_transactions)
        assert next(gen) == "Payment 1"
        assert next(gen) == "Payment 2"
        assert next(gen) == "Payment 3"
        assert next(gen) == "Payment 4"
        with pytest.raises(StopIteration):
            next(gen)

    def test_empty_transactions(self):
        gen = transaction_descriptions([])
        with pytest.raises(StopIteration):
            next(gen)


class TestCardNumberGenerator:
    @pytest.mark.parametrize(
        "start, stop, expected",
        [
            (1, 2, ["0000 0000 0000 0001"]),
            (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
            (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000"]),
        ],
    )
    def test_generator(self, start, stop, expected):
        result = list(card_number_generator(start, stop))
        assert result == expected

    def test_empty_range(self):
        assert list(card_number_generator(5, 5)) == []
