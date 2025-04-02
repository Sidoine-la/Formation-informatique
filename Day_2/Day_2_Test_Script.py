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

def test_day_2():
    exercises = {
        "exo_1.py": [
            {"input": "Alice\n", "expected_output": "Hello, Alice!"},
            {"input": "Bob\n", "expected_output": "Hello, Bob!"},
            {"input": "John\n", "expected_output": "Hello, John!"},
            {"input": "Omer\n", "expected_output": "Hello, Omer!"},
            {"input": "Charlie\n", "expected_output": "Hello, Charlie!"}
        ],
        "exo_2.py": [
            {"input": "5\n10\n", "expected_output": "Sum: 15"},
            {"input": "3\n7\n", "expected_output": "Sum: 10"},
            {"input": "10\n15\n", "expected_output": "Sum: 25"},
            {"input": "6\n4\n", "expected_output": "Sum: 10"},
            {"input": "9\n11\n", "expected_output": "Sum: 20"}
        ],
        "exo_3.py": [
            {"input": "8\n", "expected_output": "Even"},
            {"input": "9\n", "expected_output": "Odd"},
            {"input": "4\n", "expected_output": "Even"},
            {"input": "7\n", "expected_output": "Odd"},
            {"input": "10\n", "expected_output": "Even"}
        ],
        "exo_4.py": [
            {"input": "5\n9\n", "expected_output": "Largest number: 9"},
            {"input": "3\n7\n", "expected_output": "Largest number: 7"},
            {"input": "12\n8\n", "expected_output": "Largest number: 12"},
            {"input": "14\n17\n", "expected_output": "Largest number: 17"},
            {"input": "6\n6\n", "expected_output": "Largest number: 6"}
        ],
        "exo_5.py": [
            {"input": "20\n", "expected_output": "Eligible to vote"},
            {"input": "16\n", "expected_output": "Not eligible to vote"},
            {"input": "18\n", "expected_output": "Eligible to vote"},
            {"input": "25\n", "expected_output": "Eligible to vote"},
            {"input": "12\n", "expected_output": "Not eligible to vote"}
        ]
    }
    
    total_correct = 0
    total_tests = 0
    
    for exo, tests in exercises.items():
        print(colored(f"\nTesting {exo} - Day 2", "blue", attrs=["bold"]))
        results, correct, num_tests = run_test(exo, tests)
        print(tabulate(results, headers=["Test", "Input", "Output", "Expected", "Status"], tablefmt="grid"))
        
        # Mise à jour des compteurs totaux
        total_correct += correct
        total_tests += num_tests
    
    # Affichage du score total de la journée
    day_percentage = (total_correct / total_tests) * 100
    print(colored(f"\nTotal score for Day 2: {day_percentage:.2f}%", "cyan", attrs=["bold"]))

test_day_2()
