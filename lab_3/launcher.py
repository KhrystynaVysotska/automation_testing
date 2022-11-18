import os
import unittest


def load_tests(folder_name):
    loader = unittest.TestLoader()
    package_tests = loader.discover(start_dir=folder_name, pattern="test_*.py")
    standard_tests = unittest.TestSuite()
    standard_tests.addTests(package_tests)
    return standard_tests


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(load_tests(os.path.dirname(__file__)))
