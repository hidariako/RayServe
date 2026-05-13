# test_rayserve.py
"""
Tests for RayServe module.
"""

import unittest
from rayserve import RayServe

class TestRayServe(unittest.TestCase):
    """Test cases for RayServe class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RayServe()
        self.assertIsInstance(instance, RayServe)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RayServe()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
