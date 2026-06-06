#!/usr/bin/python3
"""Unittests for max_integer function."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test suite for max_integer."""

    def test_empty_list(self):
        """Test list is empty."""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test list of one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_max_at_end(self):
        """Test max is at the end."""
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_max_at_beginning(self):
        """Test max is at the beginning."""
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_in_middle(self):
        """Test max is in the middle."""
        self.assertEqual(max_integer([1, 9, 2, 3]), 9)

    def test_one_negative_number(self):
        """Test list with one negative number."""
        self.assertEqual(max_integer([-1, 2, 3]), 3)

    def test_only_negative_numbers(self):
        """Test list with only negative numbers."""
        self.assertEqual(max_integer([-10, -3, -50, -2]), -2)

    def test_all_same_numbers(self):
        """Extra safety test for duplicates."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
