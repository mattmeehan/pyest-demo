from pytest_demo.math_operations import MathOperations


def test_math_operations_add():
    mo = MathOperations()
    assert mo.add(1, 2) == 3