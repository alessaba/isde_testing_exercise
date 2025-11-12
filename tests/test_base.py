import pytest, unittest

# Pytest version

def test_example():
    assert True

def test_two_plus_two():
    assert 2 + 2 == 4


# Unittest version

class TestBase(unittest.TestCase):
    def test_unittest(self):
        self.assertTrue(True)

    def test_tpt(self):
        self.assertEqual(2 + 2, 4)