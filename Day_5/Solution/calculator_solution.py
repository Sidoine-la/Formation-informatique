def calculator():
    try:
        # Get first number
        num1 = float(input())
        
        # Get operator
        operator = input()
        
        # Get second number
        num2 = float(input())
        
        # Perform operation
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '**':
            result = num1 ** num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero")
                return
            result = num1 / num2
        else:
            print("Error: Invalid operator")
            return
        
        # Display result
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid input")

# Run the calculator
if __name__ == "__main__":
    calculator()
