# def test_int():  # Test for integer data type
#     assert 1 == 1
#
#
# def test_str():  # Test for string data type
#     assert 'str' == 'str'
#
#
# def test_float():  # Test for float data type
#     assert 1.0 == 1.0
#
#
# def test_array():  # Test for array/list format
#     assert [1, 2, 3] == [1, 2, 3]
#
#
# def test_dict():  # Test for dictionary format
#     assert {'1': 1} == {'1': 1}


"""
How the above code executed when ran with command 
    `pytest -v -s`

Exercise_Files/code_samples/pytest_test.py::test_assert_true PASSED
Exercise_Files/code_samples/test_file1.py::test_int PASSED
Exercise_Files/code_samples/test_file1.py::test_str PASSED
Exercise_Files/code_samples/test_file1.py::test_float PASSED
Exercise_Files/code_samples/test_file1.py::test_array PASSED
Exercise_Files/code_samples/test_file1.py::test_dict PASSED
"""

##############################################################################


# def test_float():
#     """
#     Test if the assert is True for a floating point value
#     """
#     assert (0.1 + 0.2) == 0.3


# """
# How the above code executed when ran with command
#     `pytest -v -s`
#
# Exercise_Files/code_samples/test_file1.py::test_float FAILED
#
# ==================== FAILURES =======================
# ___________________ test_float ______________________
#
#     def test_float():
#         """
#         Test if the assert is True for a floating point value
#         """
# >       assert (0.1 + 0.2) == 0.3
# E       assert 0.30000000000000004 == 0.3
# E         +0.30000000000000004
# E         -0.3
#
# Exercise_Files\ code_samples\ test_file1.py:40: AssertionError
# ================ short test summary info ==================
# FAILED Exercise_Files/code_samples/test_file1.py::test_float - assert 0.30000000000000004 == 0.3
# ============== 1 failed, 1 passed in 0.09s =================
# """

##############################################################################
# from pytest import approx
#
#
# def test_float():
#     """
#     Test if the assert is True for a floating point value
#         Using the `approx` statement this time
#     """
#     assert (0.1 + 0.2) == approx(0.3)


"""
How the above code executed when ran with command 
    `pytest -v -s`

Exercise_Files/code_samples/test_file1.py::test_float PASSED
"""

##############################################################################
from pytest import raises


def raises_val_execption():
    raise ValueError


def test_exception():
    with raises(ValueError):
        raises_val_execption()


"""
How the above code executed when ran with command 
    `pytest -v -s`

Exercise_Files/code_samples/test_file1.py::test_exception PASSED
"""

##############################################################################
