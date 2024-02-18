import re
from datetime import datetime


class Transaction:
    def __init__(self, transaction_id, date, state, operation_amount, description, from_account=None, to_account=None):
        self.id = transaction_id
        self.date = date
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_account = from_account
        self.to_account = to_account

    def __str__(self):
        """
        Отформатировал дату по требованиям программы
        """
        date_obj = datetime.strptime(self.date, "%Y-%m-%dT%H:%M:%S.%f")
        formatted_date = date_obj.strftime("%d.%m.%Y")

        if self.from_account is not None:
            """
            С помощью регулярного выражение разделил строку на числа и буквы
            """
            search_card_name = re.findall(r'[a-zA-Zа-яА-Я]+', self.from_account)
            card_name = ''.join(search_card_name)
            card_name = re.sub(r'([a-z])([A-Z0-9])', r'\1 \2', card_name)
            search_card_number = re.search(r"\d+", self.from_account).group()
            card_number = ''.join(search_card_number)
            formatted_card_number = card_name + " " + card_number[:4] + " " + card_number[
                                                                  4:6] + "** ****" + card_number[-4:]
        else:
            formatted_card_number = "Открытие счета"

        if self.to_account is not None:
            """
            С помощью регулярного выражение разделил строку на числа и буквы
            """
            search_account_name = re.findall(r'[a-zA-Zа-яА-Я]+', self.to_account)
            account_name = ''.join(search_account_name)
            search_account_number = re.search(r"\d+", self.to_account).group()
            account_number = ''.join(search_account_number)
            formatted_account_number = account_name + " " + "**" + account_number[-4:]
        else:
            formatted_account_number = "Открытие счета"

        return f"""
        {formatted_date} {self.description}
        {formatted_card_number} -> {formatted_account_number}
        {self.operation_amount}
        """
