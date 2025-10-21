import importlib

import pytest

EXPECTED_ANSWERS = {
    1: 233168,
    2: 4613732,
    3: 6857,
    4: 906609,
    5: 232792560,
    6: 25164150,
    7: 104743,
    8: 23514624000,
    9: 31875000,
    10: 142913828922,
}


@pytest.mark.parametrize("problem_number", EXPECTED_ANSWERS.keys(), ids=lambda s: f"problem_{s:04}")
def test_euler_solutions(problem_number: int):
    module = importlib.import_module(f"euler.p{problem_number:04}")
    answer = str(module.solve())
    expected_answer = str(EXPECTED_ANSWERS[problem_number])
    assert answer == expected_answer
