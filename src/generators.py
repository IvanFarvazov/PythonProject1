from typing import Dict, Iterable, Iterator


def filter_by_currency(transactions: Iterable[Dict], currency: str) -> Iterator[Dict]:
    return (transaction for transaction in transactions if transaction.get("currency") == currency)


def transaction_descriptions(transactions: Iterable[Dict]) -> Iterator[str]:
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    for num in range(start, stop):
        num_str = f"{num:016d}"
        yield f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"
