from typing import Any, Dict, List


def filter_by_state(operation_list: List[Dict[str, Any]], state: str = "EXECUTED") -> list[Dict[str, Any]]:
    """ "Функция сортировки по ключу state"""
    return list((item for item in operation_list if item.get("state") == state))


def sort_by_date(sort_data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция должна возвращать новый список, отсортированный по дате"""
    return sorted(sort_data, key=lambda x: str(x.get("date")), reverse=reverse)
