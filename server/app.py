#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def home():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def show_param(parameter):
    print(f'{parameter}')

    return f'{parameter}'

@app.route('/count/<int:parameter>')
def show_count(parameter):
    count = []
    for i in range(0, parameter):
        count.append(f'{str(i)}\n')
    display = ''.join(count)
    return display

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def show_math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == '%':
        return str(num1 % num2)
    elif operation == 'div':
        return str(num1 / num2)
    
