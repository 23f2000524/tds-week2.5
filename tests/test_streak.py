import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test a list with no positive numbers returns a streak of 0."""
    assert longest_positive_streak([-1, -5, 0, -2]) == 0

def test_all_positive_numbers():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak_at_beginning():
    """Test a single streak at the beginning of the list."""
    assert longest_positive_streak([2, 3, 4, 0, -1, 5]) == 3

def test_single_streak_at_end():
    """Test a single streak at the end of the list."""
    assert longest_positive_streak([-2, 0, 1, 5, 6, 7]) == 4

def test_multiple_streaks_longest_first():
    """Test with multiple streaks where the longest comes first."""
    assert longest_positive_streak([5, 6, 7, 0, 4, -1, 2, 3]) == 3

def test_multiple_streaks_longest_last():
    """Test with multiple streaks where the longest comes last."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros_and_negatives():
    """Test a mixed list of positive, zero, and negative numbers."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5, -1, 6, 7]) == 3

def test_single_element_list_positive():
    """Test a list with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_element_list_non_positive():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([-5]) == 0
    assert longest_positive_streak([0]) == 0

def test_identical_positive_numbers():
    """Test a streak of identical positive numbers."""
    assert longest_positive_streak([1, 1, 1]) == 3