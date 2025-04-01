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

def test_day_1():
    exercises = {
        "exo_1.py": [
            {"input": "", "expected_output": "Hello, World!"},
        ],
        "exo_2.py": [
            {"input": "", "expected_output": "Murielle"},
        ],
        "exo_3.py": [
            {"input": "", "expected_output": "15"},
        ],
        "exo_4.py": [
            {"input": "7.8\n", "expected_output": "Converted integer: 7"},
        ],
        "exo_5.py": [
            {"input": "", "expected_output": "<class 'bool'>"},
        ]
    }
    
    total_correct = 0
    total_tests = 0
    
    for exo, tests in exercises.items():
        print(colored(f"\nTesting {exo} - Day 1", "blue", attrs=["bold"]))
        results, correct, num_tests = run_test(exo, tests)
        print(tabulate(results, headers=["Test", "Input", "Output", "Expected", "Status"], tablefmt="grid"))
        
        # Mise à jour des compteurs totaux
        total_correct += correct
        total_tests += num_tests
    
    # Affichage du score total de la journée
    day_percentage = (total_correct / total_tests) * 100
    print(colored(f"\nTotal score for Day 1: {day_percentage:.2f}%", "cyan", attrs=["bold"]))

test_day_1()
