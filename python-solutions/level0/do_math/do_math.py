# Build a function, do_math, that takes in 3 parameters: num1 (number), num2 (number), and operator (string)

# - it uses the operator to determine what math to do to the numbers
# 	- if '+', it adds them
# 	- if '-', it subtracts them
# 	- if '*' or 'x' or 'X', it multiplies them
# 	- if '/', it divides them
# - if then returns the result
# - Example:
# 	- do_math(5,2,'*')
# 	- Return: 10

def do_math(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*' or operator == 'x' or operator == 'X':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        result = 'You entered the wrong operator'
    return result


math1 = do_math(5, 2, 'X')

print(math1)
