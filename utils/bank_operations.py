import json
from datetime import datetime

from model.transaction import Transaction

with open('../operations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

transactions = []

"""
Распарсил данные JSON в список объектов Transaction
"""
for operation_data in data:
    transaction = Transaction(operation_data["id"],
                              operation_data["date"],
                              operation_data["state"],
                              operation_data["operationAmount"]["amount"] + " " +
                              operation_data["operationAmount"]["currency"]["name"],
                              operation_data["description"],
                              operation_data.get("from"),
                              operation_data.get("to")
                              )
    transactions.append(transaction)

"""
Отфильтровал только те операции которые прошли успешно
"""
executed_transactions = [transaction for transaction in transactions if transaction.state == "EXECUTED"]
sorted_transactions = sorted(executed_transactions, key=lambda x: datetime.strptime(x.date, "%Y-%m-%dT%H:%M:%S.%f"),
                             reverse=True)

last_executed_operations = sorted_transactions[:5]

for transaction in last_executed_operations:
    print(transaction)
    print('-' * 100)
