from flask import Flask, jsonify, request

from cashman.model.expense import Expense, ExpenseSchema
from cashman.model.income import Income, IncomeSchema
from cashman.model.transaction_type import TransactionType

app = Flask(__name__)

transactions = [
  Income('Salary', 5000),
  Income('Dividends', 200),
  Expense('pizza', 50),
  Expense('Rock Concert', 100)
]


@app.route('/incomes')
def get_incomes():
  schema = IncomeSchema(many=True)
  incomes = schema.dump(
    filter(lambda t: t.type == TransactionType.INCOME, transactions)
  )
  return jsonify(incomes)


@app.route('/incomes/<int:income_idx>')
def get_income(income_idx):
  schema = IncomeSchema(many=True)
  incomes = schema.dump(
    filter(lambda t: t.type == TransactionType.INCOME, transactions)
  )
  return jsonify(incomes[income_idx])  


@app.route('/incomes', methods=['POST'])
def add_income():
  income = IncomeSchema().load(request.get_json())
  transactions.append(income)
  return "", 204


@app.route('/expenses')
def get_expenses():
  schema = ExpenseSchema(many=True)
  expenses = schema.dump(
      filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
  )
  return jsonify(expenses)


@app.route('/expenses', methods=['POST'])
def add_expense():
  expense = ExpenseSchema().load(request.get_json())
  transactions.append(expense)
  return "", 204

@app.route('/expenses/<int:expense_idx>')
def get_expense(expense_idx):
  schema = ExpenseSchema(many=True)
  expenses = schema.dump(
    filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
  )
  return jsonify(expenses[expense_idx])

if __name__ == "__main__":
    app.run()