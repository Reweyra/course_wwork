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
        date_obj = datetime.strptime(self.date, "%Y-%m-%dT%H:%M:%S.%f")
        formatted_date = date_obj.strftime("%d.%m.%Y")

        return f"""
        {formatted_date} {self.description}
        {self.from_account} -> {self.to_account}
        {self.operation_amount}
        """
