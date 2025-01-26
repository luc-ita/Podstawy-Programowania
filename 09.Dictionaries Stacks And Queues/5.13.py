stack = []

while True:
    user_input = input("Enter a value: ").strip()

    # check if input is a number
    if user_input.replace('.', '', 1).isdigit():
        stack.append(float(user_input))

    # check for operators
    elif user_input in ['+', '-', '*', '/']:
        if len(stack) < 2:
            print("Error: Not enough operands")
            continue

        # pop the two most recent operands
        b = stack.pop()
        a = stack.pop()

        # do calculation based on operator
        if user_input == '+':
            result = a + b
        elif user_input == '-':
            result = a - b
        elif user_input == '*':
            result = a * b
        elif user_input == '/':
            if b == 0:
                print("Error: Division by zero")
                continue
            result = a / b
        stack.append(result)

    # check for equals sign
    elif user_input == '=':
        if not stack:
            print("Error: No result available")
        elif len(stack) > 1:
            print("Error: Too many values left in stack")
        else:
            print(f"Result: {stack[0]}")
        break

    else:
        print("Invalid input. Please enter a number, operator, or =")

