from calculator import Calculator

def test_sequence_operations():
    calc = Calculator()
    result = calc.add(2, 3)
    result = calc.multiply(result, 2)
    assert result == 10
