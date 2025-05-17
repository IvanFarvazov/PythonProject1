from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(str_number_card_or_account: str) -> str:
    """Обрабатывает информацию о картах и о счетах"""

    if "счет" in str_number_card_or_account.lower() or "счёт" in str_number_card_or_account.lower():
        number_account = str_number_card_or_account[-20:]
        number_account_mask = get_mask_account(number_account)
        text = str(f"{str_number_card_or_account[:-21]} {number_account_mask}")

    else:
        number_card = str_number_card_or_account[-16:]
        number_card_mask = get_mask_card_number(number_card)
        text = str(f"{str_number_card_or_account[:-17]} {number_card_mask}")

    return text


print(mask_account_card("Visa 1234123412341234"))
print(mask_account_card("Visa Classic 1234123412341234"))
print(mask_account_card("Счет 12341234123412341234"))


def get_date(user_data: str) -> str:
    """Преобразование даты в формат ДД.ММ.ГГ"""
    data_obj = datetime.fromisoformat(user_data)
    formatted_data = data_obj.strftime("%d.%m.%Y")
    return formatted_data


print(get_date("2024-03-11T02:26:18.671407"))
