# def setup_function(function):
#     """
#     Creates the setup code for the test function passed in
#     This function will automatically run before each test is called
#     :param function: test function
#     :return: str: print statement
#     """
#     if function == test1:
#         print("\nSetting up Test 1!")
#
#     elif function == test2:
#         print('\nSetting up Test 2!')
#
#     else:
#         print('\nSetting up unknown Test!')
#
#
# def teardown_function(function):
#     """
#     Creates the teardown code for the test function passed in
#     This function will automatically run after each test is called
#     :param function: test function
#     :return: str: print statement
#     """
#     if function == test1:
#         print("\nTearing Down Test 1!")
#
#     elif function == test2:
#         print('\nTearing Down Test 2!')
#
#     else:
#         print('\nTearing Down unknown Test!')
#
#
# def test1():
#     """
#     A simple test function that returns true and prints a statement
#     :return: str: print statement
#     """
#     print('Executing Test 1!')
#     assert True
#
#
# def test2():
#     """
#     A simple test function that returns true and prints a statement
#     :return: str: print statement
#     """
#     print('Executing Test 2!')
#     assert True


"""
How the above code executed when ran with command
    `pytest -v -s`
    
Exercise_Files/code_samples/pytest_test.py::test_assert_true PASSED
Exercise_Files/code_samples/test_file.py::test1
Setting up Test 1!
Executing Test 1!
PASSED
Tearing Down Test 1!

Exercise_Files/code_samples/test_file.py::test2
Setting up Test 2!
Executing Test 2!
PASSED
Tearing Down Test 2!
"""

##############################################################################


# def setup_module(module):
#     """
#     This will run once before any other code is ran
#     :param module:
#     :return: str: print statement
#     """
#     print('Setup Module')
#
#
# def teardown_module(module):
#     """
#     This will run once after all code has already been ran
#     :param module:
#     :return: str: print statement
#     """
#     print('Teardown Module')
#
#
# def setup_function(function):
#     """
#     Creates the setup code for the test function passed in
#     This function will automatically run before each test is called
#     :param function: test function
#     :return: str: print statement
#     """
#     if function == test1:
#         print("\nSetting up Test 1!")
#
#     elif function == test2:
#         print('\nSetting up Test 2!')
#
#     else:
#         print('\nSetting up unknown Test!')
#
#
# def teardown_function(function):
#     """
#     Creates the teardown code for the test function passed in
#     This function will automatically run after each test is called
#     :param function: test function
#     :return: str: print statement
#     """
#     if function == test1:
#         print("\nTearing Down Test 1!")
#
#     elif function == test2:
#         print('\nTearing Down Test 2!')
#
#     else:
#         print('\nTearing Down unknown Test!')
#
#
# def test1():
#     """
#     A simple test function that returns true and prints a statement
#     :return: str: print statement
#     """
#     print('Executing Test 1!')
#     assert True
#
#
# def test2():
#     """
#     A simple test function that returns true and prints a statement
#     :return: str: print statement
#     """
#     print('Executing Test 2!')
#     assert True


"""
How the above code executed when ran with command
    `pytest -v -s`

Exercise_Files/code_samples/pytest_test.py::test_assert_true PASSED
Exercise_Files/code_samples/test_file.py::test1 Setup Module

Setting up Test 1!
Executing Test 1!
PASSED
Tearing Down Test 1!

Exercise_Files/code_samples/test_file.py::test2
Setting up Test 2!
Executing Test 2!
PASSED
Tearing Down Test 2!
Teardown Module
"""

##############################################################################

# class TestClass:
#     @classmethod
#     def setup_class(cls):
#         """
#         This will run once before any other code is ran
#         :param cls:
#         :return: str: print statement
#         """
#         print('Setup TestClass!')
#
#     @classmethod
#     def teardown_class(cls):
#         """
#         This will run once after all code has already been ran
#         :param cls:
#         :return: str: print statement
#         """
#         print('Teardown TestClass!')
#
#     def setup_method(self, method):
#         """
#         Creates the setup code for the test method passed in
#         This function will automatically run before each test is called
#         :param method: test method
#         :return: str: print statement
#         """
#         if method == self.test1:
#             print("\nSetting up Test 1!")
#
#         elif method == self.test2:
#             print('\nSetting up Test 2!')
#
#         else:
#             print('\nSetting up unknown Test!')
#
#     def teardown_method(self, method):
#         """
#         Creates the teardown code for the test method passed in
#         This function will automatically run after each test is called
#         :param method: test method
#         :return: str: print statement
#         """
#         if method == self.test1:
#             print("\nTearing Down Test 1!")
#
#         elif method == self.test2:
#             print('\nTearing Down Test 2!')
#
#         else:
#             print('\nTearing Down unknown Test!')
#
#     def test1(self):
#         """
#         A simple test method that returns true and prints a statement
#         :return: str: print statement
#         """
#         print('Executing Test 1!')
#         assert True
#
#     def test2(self):
#         """
#         A simple test function that returns true and prints a statement
#         :return: str: print statement
#         """
#         print('Executing Test 2!')
#         assert True
#

"""
How the above code executed when ran with command
    `pytest -v -s`

Exercise_Files/code_samples/pytest_test.py::test_assert_true PASSED
Exercise_Files/code_samples/test_file.py::TestClass::test1 Setup TestClass!

Setting up Test 1!
Executing Test 1!
PASSED
Tearing Down Test 1!

Exercise_Files/code_samples/test_file.py::TestClass::test2
Setting up Test 2!
Executing Test 2!
PASSED
Tearing Down Test 2!
Teardown TestClass!
"""

##############################################################################

# import pytest
#
# @pytest.fixture()
# def setup():
#     """
#     A simple setup method done as a fixture
#     :return: str: print statement
#     """
#     print('\nSetup!')
#
#
# def test1():
#     """
#     A simple test method to just print a statement and return True
#     :return: str: print statement
#     """
#     print('Executing Test 1!')
#     assert True
#
#
# def test2():
#     """
#     A simple test method to just print a statement and return True
#     :return: str: print statement
#     """
#     print('Executing Test 2!')
#     assert True


"""
How the above code executed when ran with command
    `pytest -v -s`

Exercise_Files/code_samples/pytest_test.py::test_assert_true PASSED
Exercise_Files/code_samples/test_file.py::test1 Executing Test 1!
PASSED
Exercise_Files/code_samples/test_file.py::test2 Executing Test 2!
PASSED
"""

##############################################################################

# import pytest
#
# @pytest.fixture()
# def setup():
#     """
#     A simple setup method done as a fixture
#     :return: str: print statement
#     """
#     print('\nSetup!')
#
#
# def test1(setup):  # Just added setup fixture here to see what happens
#     """
#     A simple test method to just print a statement and return True
#     :return: str: print statement
#     """
#     print('Executing Test 1!')
#     assert True
#
#
# def test2():
#     """
#     A simple test method to just print a statement and return True
#     :return: str: print statement
#     """
#     print('Executing Test 2!')
#     assert True


"""
How the above code executed when ran with command
    `pytest -v -s`

Exercise_Files/code_samples/pytest_test.py::test_assert_true PASSED
Exercise_Files/code_samples/test_file.py::test1
Setup!
Executing Test 1!
PASSED
Exercise_Files/code_samples/test_file.py::test2 Executing Test 2!
PASSED
Exercise_Files/code_samples/test_file.py::test2 Executing Test 2!
PASSED
"""

##############################################################################

# import pytest
#
# @pytest.fixture()
# def setup():
#     """
#     A simple setup method done as a fixture
#     :return: str: print statement
#     """
#     print('\nSetup!')
#
#
# def test1(setup):  # Just added setup fixture here to see what happens
#     """
#     A simple test method to just print a statement and return True
#     :return: str: print statement
#     """
#     print('Executing Test 1!')
#     assert True
#
#
# # Added the fixture to test2 using the decorator, this is just another way
# #   to do the same thing as we did in the test1 function
# @pytest.mark.usefixtures('setup')
# def test2():
#     """
#     A simple test method to just print a statement and return True
#     :return: str: print statement
#     """
#     print('Executing Test 2!')
#     assert True


"""
How the above code executed when ran with command
    `pytest -v -s`

Exercise_Files/code_samples/pytest_test.py::test_assert_true PASSED
Exercise_Files/code_samples/test_file.py::test1
Setup!
Executing Test 1!
PASSED
Exercise_Files/code_samples/test_file.py::test2
Setup!
Executing Test 2!
PASSED
"""

##############################################################################

# import pytest
#
#
# # If all the test will be using the same fixture, use the `autouse` parameter
# @pytest.fixture(autouse=True)
# def setup():
#     """
#     A simple setup method done as a fixture
#     :return: str: print statement
#     """
#     print('\nSetup!')
#
#
# def test1():
#     """
#     A simple test method to just print a statement and return True
#     :return: str: print statement
#     """
#     print('Executing Test 1!')
#     assert True
#
#
# def test2():
#     """
#     A simple test method to just print a statement and return True
#     :return: str: print statement
#     """
#     print('Executing Test 2!')
#     assert True


"""
How the above code executed when ran with command
    `pytest -v -s`

Exercise_Files/code_samples/pytest_test.py::test_assert_true PASSED
Exercise_Files/code_samples/test_file.py::test1
Setup!
Executing Test 1!
PASSED
Exercise_Files/code_samples/test_file.py::test2
Setup!
Executing Test 2!
PASSED
"""

##############################################################################

# import pytest
#
#
# @pytest.fixture()
# def setup1():
#     """
#     Setup fixture using the "yield" method teardown
#     :return: str: print statement
#     """
#     print('Setup 1!')
#     yield
#     print('Teardown 1!')
#
#
#
# @pytest.fixture()
# def setup2(request):
#     """
#     Setup fixture using the request-context's "addfinalizer" teardown method
#     :param request:
#     :return:
#     """
#     print('Setup 2!')
#
#     def teardown_a():
#         print('\nTeardown A!')
#
#     def teardown_b():
#         print('\nTeardown b!')
#
#     request.addfinalizer(teardown_a)
#     request.addfinalizer(teardown_b)
#
#
# def test1(setup1):
#     """
#     A simple test function to just print a statement and return True
#     This function will use the setup1 fixture that uses the "yield" teardown
#     :return: str: print statement
#     """
#     print('Executing Test 1!')
#     assert True
#
#
# def test2(setup2):
#     """
#     A simple test function to just print a statement and return True
#     This function will use the setup2 fixture that uses "addfinalizer"
#     :return: str: print statement
#     """
#     print('Executing Test 2!')
#     assert True


"""
How the above code executed when ran with command
    `pytest -v -s`

Exercise_Files/code_samples/pytest_test.py::test_assert_true PASSED
Exercise_Files/code_samples/test_file.py::test1 Setup 1!
Executing Test 1!
PASSEDTeardown 1!

Exercise_Files/code_samples/test_file.py::test2 Setup 2!
Executing Test 2!
PASSED
Teardown b!

Teardown A!
"""

##############################################################################

# import pytest
#
#
# @pytest.fixture(scope='session', autouse=True)
# def setup_session():
#     """
#     Sets up the fixture in the "session" scope
#     :return: str: print statement
#     """
#     print('\nSetup Session')
#
#
# @pytest.fixture(scope='module', autouse=True)
# def setup_module():
#     """
#     Sets up the fixture in the "module" scope
#     :return: str: print statement
#     """
#     print('\nSetup Module')
#
#
# @pytest.fixture(scope='function', autouse=True)
# def setup_function():
#     """
#     Sets up the fixture in the "function" scope
#     :return: str: print statement
#     """
#     print('\nSetup Function')
#
#
# def test1():
#     """
#     A simple test method to just print a statement and return True
#     :return: str: print statement
#     """
#     print('Executing Test 1!')
#     assert True
#
#
# def test2():
#     """
#     A simple test method to just print a statement and return True
#     :return: str: print statement
#     """
#     print('Executing Test 2!')
#     assert True
#

"""
How the above code, along with code from test_file2.py lines 1-79, 
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

# import pytest
#
#
# @pytest.fixture(params=[1, 2, 3])
# def setup(request):
#     """
#     Creates a setup fixture that uses data given for tests
#     :param request:
#     :return: the data given in the params argument in the decorator
#     """
#     ret_val = request.param
#     print(f'\nSetup! ret_val = {ret_val}')
#     return ret_val
#
#
# def test1(setup):
#     """
#     Test function calling on the fixture to use its given data
#     :param setup: fixture method
#     :return: str: print statement
#     """
#     print(f'\nSetup = {setup}')
#     assert True


"""
How the above code executed when ran with command 
    `pytest -v -s`

Exercise_Files/code_samples/pytest_test.py::test_assert_true PASSED
Exercise_Files/code_samples/test_file.py::test1[1]
Setup! ret_val = 1

Setup = 1
PASSED
Exercise_Files/code_samples/test_file.py::test1[2]
Setup! ret_val = 2

Setup = 2
PASSED
Exercise_Files/code_samples/test_file.py::test1[3]
Setup! ret_val = 3

Setup = 3
PASSED
"""

##############################################################################

