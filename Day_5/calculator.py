def calculator():
    try:
        num1 = float(input(" "))
        operator = input(" ").strip()
        
        num2 = float(input(" "))
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero")
                return
            result = num1 / num2
        elif operator == "**":
            result = num1 ** num2
        else:
            print("Error: Invalid operator")
            return  
        
        print(f"Result: {result}")
    
    except ValueError:
        print(" Error: Invalid input ")
        
calculator()