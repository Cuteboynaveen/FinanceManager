from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

income = 0
expenses = {}
balance = 0

@app.route('/add_income', methods=['POST'])
def add_income():
    global income, balance
    amount = int(request.form['amount'])
    income += amount
    balance += amount
    return jsonify({'data': {'income': income, 'expenses': expenses, 'balance': balance}})

@app.route('/add_expense', methods=['POST'])
def add_expense():
    global expenses, balance
    category = request.form['category']
    amount = int(request.form['amount'])
    expenses[category] = expenses.get(category, 0) + amount
    balance -= amount
    return jsonify({'data': {'income': income, 'expenses': expenses, 'balance': balance}})

@app.route('/display_finances')
def display_finances():
    expense_categories = '\n'.join(f'{category}: ${amount}' for category, amount in expenses.items())
    return jsonify({'data': {'income': income, 'expenses': expense_categories, 'balance': balance}})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)