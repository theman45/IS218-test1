"""Tests for arithmetic operations."""

from src import operations

def test_add():
    """Test addition of numbers."""
    assert operations.add(2, 3) == 5
    assert operations.add(-1, 1) == 0

def test_subtract():
    """Test subtraction of numbers."""
    assert operations.subtract(5, 3) == 2
    assert operations.subtract(3, 5) == -2
