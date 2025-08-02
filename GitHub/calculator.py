def switch(value):
    if value == '+':
        return a + b
    elif value == '-':
        return a - b
    elif value == '*':
        return a * b
    elif value == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operator"

print("What is the 1st number?")
a = int(input())

print("What is the operator?")
value = input()

print("What is the 2nd number?")
b = int(input())

# Store the result in a variable
ans = switch(value)

print("Result:", ans)
