"""
A test module that tests multiply_numbers function with edge cases
like Inf, NaN, and non-numeric inputs.
"""

from pyospackage_kkalinin.example import multiply_numbers

#from example import multiply_numbers
#from pyospackage_kkalinin.example import multiply_numbers
#from src.pyospackage_kkalinin.example import multiply_numbers
import math

def test_multiply_numbers_with_infinity():
    """
    Test multiply_numbers when one number is infinity.
    """
    out = multiply_numbers(float('inf'), 5)
    expected_out = float('inf')
    assert out == expected_out, f"Expected {expected_out} but got {out}"

def test_multiply_numbers_with_negative_infinity():
    """
    Test multiply_numbers when one number is negative infinity.
    """
    out = multiply_numbers(float('-inf'), 5)
    expected_out = float('-inf')
    assert out == expected_out, f"Expected {expected_out} but got {out}"

def test_multiply_numbers_infinity_by_zero():
    """
    Test multiply_numbers infinity by zero - results in NaN.
    """
    out = multiply_numbers(float('inf'), 0)
    # Infinity * 0 = NaN (Not a Number)
    assert math.isnan(out), f"Expected NaN but got {out}"

def test_multiply_numbers_with_nan():
    """
    Test multiply_numbers when one number is NaN.
    """
    out = multiply_numbers(float('nan'), 5)
    assert math.isnan(out), f"Expected NaN but got {out}"

def test_multiply_numbers_both_nan():
    """
    Test multiply_numbers when both numbers are NaN.
    """
    out = multiply_numbers(float('nan'), float('nan'))
    assert math.isnan(out), f"Expected NaN but got {out}"

def test_multiply_numbers_with_string_numeric():
    """
    Test multiply_numbers with numeric strings (should work in Python).
    """
    out = multiply_numbers("3", "5")
    expected_out = 15
    assert out == expected_out, f"Expected {expected_out} but got {out}"

def test_multiply_numbers_with_string_float():
    """
    Test multiply_numbers with string containing float.
    """
    out = multiply_numbers("2.5", "4")
    expected_out = 10.0
    assert out == expected_out, f"Expected {expected_out} but got {out}"

def test_multiply_numbers_with_non_numeric_string():
    """
    Test multiply_numbers with non-numeric string - SHOULD RAISE ERROR.
    """
    try:
        out = multiply_numbers("hello", 5)
        # If we get here, test fails because it didn't raise an error
        assert False, f"Expected TypeError but got {out}"
    except TypeError:
        # This is the expected behavior
        pass

def test_multiply_numbers_with_none():
    """
    Test multiply_numbers with None - SHOULD RAISE ERROR.
    """
    try:
        out = multiply_numbers(None, 5)
        assert False, f"Expected TypeError but got {out}"
    except TypeError:
        # This is the expected behavior
        pass

def test_multiply_numbers_mixed_types():
    """
    Test multiply_numbers with mixed valid/invalid types.
    """
    try:
        out = multiply_numbers("abc", 5)
        assert False, f"Expected TypeError but got {out}"
    except TypeError:
        pass

def test_multiply_numbers_very_large_numbers():
    """
    Test multiply_numbers with very large numbers (edge of overflow).
    """
    out = multiply_numbers(1e308, 1e308)
    # This will become inf in Python
    expected_out = float('inf')
    assert out == expected_out, f"Expected {expected_out} but got {out}"