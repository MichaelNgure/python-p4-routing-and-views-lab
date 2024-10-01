#!/usr/bin/env python3

# import module
from flask import Flask, Response

# instantiate
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return parameter


@app.route('/count/<int:parameter>')
def count(parameter):
    # Generate numbers from 0 to parameter - 1
    numbers = "\n".join(str(i) for i in range(parameter))
    
    # Append a newline at the end
    numbers += "\n"
    
    # Return the result with appropriate content type
    return Response(numbers, content_type='text/plain')

@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    # can use match...case
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
        return str(num1 / num2)
    elif operation == "%":
        return str(num1 % num2)
    else:
        return "<h1>Invalid operation!</h1>"


if __name__ == '__main__':
    app.run(port=5555, debug=True)