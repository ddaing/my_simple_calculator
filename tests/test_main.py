import pytest

from simple_calculator.main import SimpleCalculator


def test_add_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(4, 5)

    assert result == 9


def test_add_three_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(4, 5, 6)

    assert result == 15


def test_add_many_numbers():
    numbers = range(100)

    calculator = SimpleCalculator()

    result = calculator.add(*numbers)

    assert result == 4950


def test_subtract_two_numbers():

    calculator = SimpleCalculator()

    result = calculator.sub(10, 3)

    assert result == 7


def test_mul_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.mul(6, 4)

    assert result == 24


def test_mul_many_numbers():
    numbers = range(1, 10)

    calculator = SimpleCalculator()

    result = calculator.mul(*numbers)

    assert result == 362880


def test_div_two_numbers_float():
    calculator = SimpleCalculator()

    result = calculator.div(13, 2)

    assert result == 6.5


def test_div_by_zero_returns_inf():
    calculator = SimpleCalculator()

    result = calculator.div(5, 0)

    assert result == float("inf")


def test_mul_by_zero_raises_exception():
    calculator = SimpleCalculator()

    with pytest.raises(ValueError):
        calculator.mul(3, 0)

def test_avg_1():
    calculator = SimpleCalculator()

    result = calculator.avg([2, 5, 12, 98])

    assert result == 29.25


def test_avg_2():
    calculator = SimpleCalculator()

    result = calculator.avg([2, 5, 12, 98], ut=90)

    assert result == calculator.avg([2, 5, 12])


def test_avg_3():
    calculator = SimpleCalculator()

    result = calculator.avg([2, 5, 12, 98], lt=10)

    assert result == calculator.avg([12, 98])


def test_avg_4():
    calculator = SimpleCalculator()

    result = calculator.avg([2, 5, 12, 98], ut=98)

    assert result == calculator.avg([2, 5, 12, 98])


def test_avg_5():
    calculator = SimpleCalculator()

    result = calculator.avg([2, 5, 12, 98], lt=5)

    assert result == calculator.avg([5, 12, 98])


def test_avg_6():
    calculator = SimpleCalculator()

    result = calculator.avg([])

    assert result == 0


def test_avg_7():
    calculator = SimpleCalculator()

    result = calculator.avg([12, 98], lt=15, ut=90)

    assert result == 0


def test_avg_8():
    calculator = SimpleCalculator()

    result = calculator.avg([], lt=15, ut=90)

    assert result == 0


def test_avg_9():
    calculator = SimpleCalculator()

    result = calculator.avg([-1, 0, 1], lt=0)

    assert result == 0.5


def test_avg_10():
    calculator = SimpleCalculator()

    result = calculator.avg([-1, 0, 1], ut=0)

    assert result == -0.5
