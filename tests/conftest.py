import pytest


@pytest.fixture
def operation_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sample_transactions():
    return [
        {"currency": "USD", "description": "Payment 1", "amount": 100},
        {"currency": "EUR", "description": "Payment 2", "amount": 200},
        {"currency": "USD", "description": "Payment 3", "amount": 300},
        {"currency": "GBP", "description": "Payment 4", "amount": 400},
    ]
