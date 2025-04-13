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

def color_score(score):
    if score <= 20:
        return colored(f"{score:.2f}%", "red", attrs=["bold"])
    elif 21 <= score <= 74:
        return colored(f"{score:.2f}%", "yellow", attrs=["bold"])
    else:
        return colored(f"{score:.2f}%", "green", attrs=["bold"])

def test_day_6():
    exercises = {
        "exo_1.py": [
            {"input": "Apple,Banana,Cherry,Date,Elderberry\n", "expected_output": "Banana"},
            {"input": "Mango,Pineapple,Kiwi\n", "expected_output": "Pineapple"},
        ],
        "exo_2.py": [
            {"input": "Apple,Banana,Cherry\n", "expected_output": "['Apple', 'Banana', 'Cherry', 'Mango']"},
            {"input": "Orange,Kiwi\n", "expected_output": "['Orange', 'Kiwi', 'Mango']"},
        ],
        "exo_3.py": [
            {"input": "Banana,Apple,Mango\n", "expected_output": "['Apple', 'Banana', 'Mango']"},
            {"input": "Grapes,Cherry,Fig\n", "expected_output": "['Cherry', 'Fig', 'Grapes']"},
        ],
        "exo_4.py": [
            {"input": "Apple,Banana,Mango\nBanana\n", "expected_output": "['Apple', 'Mango']"},
            {"input": "Orange,Pineapple,Kiwi\nKiwi\n", "expected_output": "['Orange', 'Pineapple']"},
        ],
        "exo_5.py": [
            {"input": "Apple,Banana,Mango\n", "expected_output": "Mango"},
            {"input": "Orange,Papaya,Guava\n", "expected_output": "Guava"},
        ]
    }
    
    total_correct = 0
    total_tests = 0
    
    for exo, tests in exercises.items():
        print(colored(f"\nTesting {exo} - Day 6", "blue", attrs=["bold"]))
        results, correct, num_tests = run_test(exo, tests)
        print(tabulate(results, headers=["Test", "Input", "Output", "Expected", "Status"], tablefmt="grid"))
        
        total_correct += correct
        total_tests += num_tests
    
    final_score = (total_correct / total_tests) * 100
    print(colored("\nFinal Day 6 Score:", "magenta", attrs=["bold"]), color_score(final_score))

test_day_6()
