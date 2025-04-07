import subprocess
from tabulate import tabulate
from termcolor import colored

def run_test(file, test_cases):
    results = []
    correct = 0
    for i, test in enumerate(test_cases, 1):
        try:
            result = subprocess.run(
                ["python3", file],
                input=test["input"],
                text=True,
                capture_output=True,
                timeout=3
            )
            
            output = result.stdout.strip().split("\n")[-1]
            expected = test["expected_output"].strip()
            
            if output == expected:
                status = colored("✅ Pass", "green")
                correct += 1
            else:
                status = colored("❌ Fail", "red")
                
            results.append([f"Test {i}", test["input"].strip(), output, expected, status])
        
        except Exception as e:
            results.append([f"Test {i}", test["input"].strip(), "Error", str(e), colored("❌ Fail", "red")])
    
    # Calcul du pourcentage de réussite pour cet exercice
    exercise_percentage = (correct / len(test_cases)) * 100
    color = "red" if exercise_percentage <= 20 else "yellow" if exercise_percentage <= 74 else "green"
    results.append([colored("Total for this exercise", "yellow"), "", "", f"{exercise_percentage:.2f}%", colored("", color)])
    
    return results, correct, len(test_cases)

def test_calculator():
    test_cases = [
        {"input": "5\n+\n3\n", "expected_output": "Result: 8.0"},
        {"input": "10\n-\n4\n", "expected_output": "Result: 6.0"},
        {"input": "6\n*\n7\n", "expected_output": "Result: 42.0"},
        {"input": "8\n/\n2\n", "expected_output": "Result: 4.0"},
        {"input": "5\n**\n3\n", "expected_output": "Result: 125.0"},
        {"input": "10\n/\n0\n", "expected_output": "Error: Cannot divide by zero"},
        {"input": "abc\n+\n3\n", "expected_output": "Error: Invalid input"},
        {"input": "7\n?\n2\n", "expected_output": "Error: Invalid operator"},
        {"input": "-5\n+\n-3\n", "expected_output": "Result: -8.0"},
        {"input": "3.5\n*\n2\n", "expected_output": "Result: 7.0"},
        {"input": "5\n+\n3\n", "expected_output": "Result: 8.0"},
        {"input": "10\n-\n2\n", "expected_output": "Result: 8.0"},
        {"input": "4\n*\n2\n", "expected_output": "Result: 8.0"},
        {"input": "16\n/\n2\n", "expected_output": "Result: 8.0"},
        {"input": "2\n**\n3\n", "expected_output": "Result: 8.0"},
        {"input": "5.5\n+\n2.5\n", "expected_output": "Result: 8.0"},
        {"input": "-5\n+\n-3\n", "expected_output": "Result: -8.0"},
        {"input": "-4\n*\n2\n", "expected_output": "Result: -8.0"},
        {"input": "-16\n/\n2\n", "expected_output": "Result: -8.0"},
        {"input": "0\n+\n8\n", "expected_output": "Result: 8.0"},
        {"input": "5\n/\n0\n", "expected_output": "Error: Cannot divide by zero"},
        {"input": "2\n&\n3\n", "expected_output": "Error: Invalid operator"},
        {"input": "abc\n+\n3\n", "expected_output": "Error: Invalid input"},
        {"input": "5\n+\n3.5\n", "expected_output": "Result: 8.5"},
        {"input": "10\n-\n10\n", "expected_output": "Result: 0.0"},
        {"input": "7\n*\n-1\n", "expected_output": "Result: -7.0"},
        {"input": "100\n/\n4\n", "expected_output": "Result: 25.0"},
        {"input": "3.3\n*\n3\n", "expected_output": "Result: 9.9"},
        {"input": "50\n-\n25.5\n", "expected_output": "Result: 24.5"},
        {"input": "6\n**\n2\n", "expected_output": "Result: 36.0"}
    ]
    
    print(colored("\nTesting Calculator Mini Project", "blue", attrs=["bold"]))
    results, correct, num_tests = run_test("calculator.py", test_cases)
    print(tabulate(results, headers=["Test", "Input", "Output", "Expected", "Status"], tablefmt="grid"))
    
    # Affichage du score total
    total_percentage = (correct / num_tests) * 100
    color = "red" if total_percentage <= 20 else "yellow" if total_percentage <= 74 else "green"
    print(colored(f"\nTotal score: {total_percentage:.2f}%", color, attrs=["bold"]))

test_calculator()
