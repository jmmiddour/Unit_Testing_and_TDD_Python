# import pytest
#
#
# @pytest.fixture(scope='module', autouse=True)
# def setup_module2():
#     """
#     Sets up the fixture in the "module" scope
#     :return: str: print statement
#     """
#     print('\nSetup Module 2')
#
#
# @pytest.fixture(scope='class', autouse=True)
# def setup_class2():
#     """
#     Sets up the fixture in the "class" scope
#     :return: str: print statement
#     """
#     print('\nSetup Class 2')
#
#
# @pytest.fixture(scope='function', autouse=True)
# def setup_function2():
#     """
#     Sets up the fixture in the "function" scope
#     :return: str: print statement
#     """
#     print('\nSetup Function 2')
#
#
# class TestClass:
#     def test_it(self):
#         """
#         A simple test method to just print a statement and return True
#         :return: str: print statement
#         """
#         print('Test It!')
#         assert True
#
#     def test_it2(self):
#         """
#         A simple test method to just print a statement and return True
#         :return: str: print statement
#         """
#         print('Test It 2!')
#         assert True


"""
How the above code, along with code from test_file.py lines 512-592, 
    executed when ran with command `pytest -v -s`

Exercise_Files/code_samples/pytest_test.py::test_assert_true PASSED
Exercise_Files/code_samples/test_file.py::test1
Setup Session

Setup Module

Setup Function
Executing Test 1!
PASSED
Exercise_Files/code_samples/test_file.py::test2
Setup Function
Executing Test 2!
PASSED
Exercise_Files/code_samples/test_file2.py::TestClass::test_it
Setup Module 2

Setup Class 2

Setup Function 2
Test It!
PASSED
Exercise_Files/code_samples/test_file2.py::TestClass::test_it2
Setup Function 2
Test It 2!
PASSED
"""

##############################################################################

