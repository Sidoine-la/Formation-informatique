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
    results.append([colored("Total for this exercise", "yellow"), "", "", f"{exercise_percentage:.2f}%", ""])
    
    return results, correct, len(test_cases)

def test_day_3():
    exercises = {
        "exo_1.py": [
            {"input": "5\n3\n", "expected_output": "15"},
            {"input": "7\n2\n", "expected_output": "14"},
            {"input": "10\n10\n", "expected_output": "100"},
            {"input": "1\n0\n", "expected_output": "0"},
            {"input": "6\n4\n", "expected_output": "24"}
        ],
        "exo_2.py": [
            {"input": "4\n", "expected_output": "16"},
            {"input": "9\n", "expected_output": "81"},
            {"input": "0\n", "expected_output": "0"},
            {"input": "-3\n", "expected_output": "9"},
            {"input": "2\n", "expected_output": "4"}
        ],
        "exo_3.py": [
            {"input": "Hello\n", "expected_output": "5"},
            {"input": "Python\n", "expected_output": "6"},
            {"input": "A\n", "expected_output": "1"},
            {"input": "12345\n", "expected_output": "5"},
            {"input": "OpenAI\n", "expected_output": "6"}
        ],
        "exo_4.py": [
            {"input": "hello world\n", "expected_output": "HELLO WORLD"},
            {"input": "python is fun\n", "expected_output": "PYTHON IS FUN"},
            {"input": "12345\n", "expected_output": "12345"},
            {"input": "aBcD\n", "expected_output": "ABCD"},
            {"input": "!@#$\n", "expected_output": "!@#$"}
        ],
        "exo_5.py": [
            {"input": "-3\n", "expected_output": "Negative"},
            {"input": "0\n", "expected_output": "Zero"},
            {"input": "10\n", "expected_output": "Positive"},
            {"input": "-1\n", "expected_output": "Negative"},
            {"input": "5\n", "expected_output": "Positive"}
        ]
    }
    
    total_correct = 0
    total_tests = 0
    
    for exo, tests in exercises.items():
        print(colored(f"\nTesting {exo} - Day 3", "blue", attrs=["bold"]))
        results, correct, num_tests = run_test(exo, tests)
        print(tabulate(results, headers=["Test", "Input", "Output", "Expected", "Status"], tablefmt="grid"))
        
        # Mise à jour des compteurs totaux
        total_correct += correct
        total_tests += num_tests
    
    # Affichage du score total de la journée
    day_percentage = (total_correct / total_tests) * 100
    print(colored(f"\nTotal score for Day 3: {day_percentage:.2f}%", "cyan", attrs=["bold"]))

test_day_3()
