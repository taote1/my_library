 # module3.py
import math

def power(base, exponent):
    """Возводит число в степень"""
    return base ** exponent

def square_root(number):
    """Находит квадратный корень числа"""
    if number < 0:
        raise ValueError("Невозможно вычислить квадратный корень из отрицательного числа")
    return math.sqrt(number)
 
