"""Tests for arithmetic operations."""

from src import operations

def test_add():
    """Test addition of numbers."""
    assert operations.add(2, 3) == 5
    assert operations.add(-1, 1) == 0
