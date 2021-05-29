# Import pytest from the python built in library
import pytest

###############################################################################

# # GREEN PHASE 1 - Step 2 -
# #     Just make the failing test pass with minimal production code
# def fizzBuzz(value):
#     """
#     Only implementing what is needed to make the test_can_call_fizzbuzz pass
#     :param value: int: any number
#     :return: nothing right now
#     """
#     return
#
#
# # RED PHASE 1 - First failing test case
# def test_can_call_fizzbuzz():
#     """
#     This test case will just verify that we can call the fizzBuzz
#         function which does not exist yet.
#     :return: Passes or Fails
#     """
#     fizzBuzz(1)

###############################################################################

# # GREEN PHASE 2 - Step 2 -
# #     Just make the failing test pass with minimal production code
# def fizzBuzz(value):
#     """
#     Only implementing what is needed to make the test_returns_value pass
#     :param value: int: any number
#     :return: "1"
#     """
#     return "1"
#
#
# # RED PHASE 2 - Step 1 - failing test case
# def test_returns_value():
#     """
#     This test case will verify we get 1 when passing in 1 as the argument
#         in the function
#     :return: Passes or Fails
#     """
#     retval = fizzBuzz(1)
#     assert retval == "1"

###############################################################################

# # GREEN PHASE 3 - Step 2 -
# #     Just make the failing test pass with minimal production code
# def fizzBuzz(value):
#     """
#     Only implementing what is needed to make the test_returns_value pass
#     :param value: int: any number
#     :return: str: the value given as the argument
#     """
#     return str(value)
#
#
# # Create a utility (helper) function to us in the test
# def checkFizzBuzz(value, expectedRetVal):
#     """
#     Helper function to check that values are being handled properly
#         withing the fizzBuzz function.
#     :param value: int: any number
#     :param expectedRetVal: str: the same number as the value as a string
#     :return: bool: True or False
#     """
#     retVal = fizzBuzz(value)        # Assign a variable to function call
#     assert retVal == expectedRetVal     # Verify the correct output
#
#
# # RED PHASE 3 - Step 1 - failing test case
# def test_returns_value():
#     """
#     This test case will verify we get 1 when passing in 1 as the argument
#         into the function or 2 if passing in 2
#     :return: bool: True or False
#     """
#     checkFizzBuzz(2, "2")   # Verifies output using helper function
#     checkFizzBuzz(1, "1")   # Verifies output using helper function

###############################################################################

# # GREEN PHASE 4 - Step 2 -
# #     Just make the failing test pass with minimal production code
# def fizzBuzz(value):
#     """
#     Only implementing what is needed to make the test_returns_fizz pass
#     :param value: int: any number
#     :return: str: "Fizz" or the value entered as the argument
#     """
#     if value == 3:      # Checks if the value is 3...
#         return "Fizz"   # Return "Fizz"
#     return str(value)   # Otherwise return the value give as a string
#
#
# # Create a utility (helper) function to us in the test
# def checkFizzBuzz(value, expectedRetVal):
#     """
#     Helper function to check that values are being handled properly
#         withing the fizzBuzz function.
#     :param value: int: any number
#     :param expectedRetVal: str: the output expected
#     :return: bool: True or False
#     """
#     retVal = fizzBuzz(value)        # Assign a variable to function call
#     assert retVal == expectedRetVal     # Verify the correct output
#
#
# # RED PHASE 4 - Step 1 - failing test case
# def test_returns_fizz():
#     """
#     This test case will verify we get "fizz" when passing in 3 as the arg
#     :return: bool: True or False
#     """
#     checkFizzBuzz(3, "Fizz")   # Verifies output using helper function

###############################################################################

# # GREEN PHASE 4 - Step 2 -
# #     Just make the failing test pass with minimal production code
# def fizzBuzz(value):
#     """
#     Only implementing what is needed to make the test_returns_buzz pass
#     :param value: int: any number
#     :return: str: "Fizz" or the value entered as the argument
#     """
#     if value == 3:      # Checks if the value is 3...
#         return "Fizz"   # Return "Fizz"
#
#     if value == 5:      # Checks if the value is 5...
#         return "Buzz"   # Return "Buzz"
#
#     return str(value)   # Otherwise return the value give as a string
#
#
# # Create a utility (helper) function to us in the test
# def checkFizzBuzz(value, expectedRetVal):
#     """
#     Helper function to check that values are being handled properly
#         withing the fizzBuzz function.
#     :param value: int: any number
#     :param expectedRetVal: str: the output expected
#     :return: bool: True or False
#     """
#     retVal = fizzBuzz(value)        # Assign a variable to function call
#     assert retVal == expectedRetVal     # Verify the correct output
#
#
# # RED PHASE 4 - Step 1 - failing test case
# def test_returns_buzz():
#     """
#     This test case will verify we get "buzz" when passing in 5 as the arg
#     :return: bool: True or False
#     """
#     checkFizzBuzz(5, "Buzz")   # Verifies output using helper function

###############################################################################

# # GREEN PHASE 5 - Step 2 -
# #     Just make the failing test pass with minimal production code
# def fizzBuzz(value):
#     """
#     Only implementing what is needed to make the test_returns_fizz6 pass
#     :param value: int: any number
#     :return: str: "Fizz" or the value entered as the argument
#     """
#     if (value % 3) == 0:      # Checks if the value is a multiple of 3...
#         return "Fizz"   # Return "Fizz"
#
#     if value == 5:      # Checks if the value is 5...
#         return "Buzz"   # Return "Buzz"
#
#     return str(value)   # Otherwise return the value give as a string
#
#
# # Create a utility (helper) function to us in the test
# def checkFizzBuzz(value, expectedRetVal):
#     """
#     Helper function to check that values are being handled properly
#         withing the fizzBuzz function.
#     :param value: int: any number
#     :param expectedRetVal: str: the output expected
#     :return: bool: True or False
#     """
#     retVal = fizzBuzz(value)        # Assign a variable to function call
#     assert retVal == expectedRetVal     # Verify the correct output
#
#
# # RED PHASE 5 - Step 1 - failing test case
# def test_returns_fizz6():
#     """
#     This test case will verify we get "fizz" when passing in 6 as the arg
#     :return: bool: True or False
#     """
#     checkFizzBuzz(6, "Fizz")   # Verifies output using helper function

###############################################################################

# # GREEN PHASE 6 - Step 2 -
# #     Just make the failing test pass with minimal production code
# def fizzBuzz(value):
#     """
#     Only implementing what is needed to make the test_returns_buzz10 pass
#     :param value: int: any number
#     :return: str: "Fizz" or the value entered as the argument
#     """
#     if isMultiple(value, 3):      # Checks if the value is a multiple of 3...
#         return "Fizz"   # Return "Fizz"
#
#     if isMultiple(value, 5):      # Checks if the value is 5...
#         return "Buzz"   # Return "Buzz"
#
#     return str(value)   # Otherwise return the value give as a string
#
#
# # Create a utility (helper) function to use in the test
# def checkFizzBuzz(value, expectedRetVal):
#     """
#     Helper function to check that values are being handled properly
#         withing the fizzBuzz function.
#     :param value: int: any number
#     :param expectedRetVal: str: the output expected
#     :return: bool: True or False
#     """
#     retVal = fizzBuzz(value)        # Assign a variable to function call
#     assert retVal == expectedRetVal     # Verify the correct output
#
#
# # Create a utility (helper) function to use in the test
# def is_multiple(value, mod):
#     """
#     This function will verify if the value given can evenly be multiplied
#         by the mod given
#     :param value: int: any number
#     :param mod: int: number to multiple value by
#     :return: bool: True or False
#     """
#     return (value % mod) == 0
#
#
# # RED PHASE 6 - Step 1 - failing test case
# def test_returns_buzz10():
#     """
#     This test case will verify we get "buzz" when passing in 10 as the arg
#     :return: bool: True or False
#     """
#     checkFizzBuzz(10, "Buzz")   # Verifies output using helper function

###############################################################################

# # GREEN PHASE 7 - Step 2 -
# #     Just make the failing test pass with minimal production code
# def fizzBuzz(value):
#     """
#     Only implementing what is needed to make the test_returns_fizzbuzz pass
#     :param value: int: 15
#     :return: str: "FizzBuzz" or the value entered as the argument
#     """
#     if isMultiple(value, 3):      # Checks if the value is a multiple of 3...
#         if isMultiple(value, 5):  # Checks if the value is a multiple of 5 also...
#             return "FizzBuzz"     # Returns "FizzBuzz" if both are true
#
#         return "Fizz"   # Return "Fizz"
#
#     if isMultiple(value, 5):      # Checks if the value is 5...
#         return "Buzz"   # Return "Buzz"
#
#     return str(value)   # Otherwise return the value give as a string
#
#
# # Create a utility (helper) function to use in the test
# def checkFizzBuzz(value, expectedRetVal):
#     """
#     Helper function to check that values are being handled properly
#         withing the fizzBuzz function.
#     :param value: int: any number
#     :param expectedRetVal: str: the output expected
#     :return: bool: True or False
#     """
#     retVal = fizzBuzz(value)        # Assign a variable to function call
#     assert retVal == expectedRetVal     # Verify the correct output
#
#
# # Create a utility (helper) function to use in the test
# def is_multiple(value, mod):
#     """
#     This function will verify if the value given can evenly be multiplied
#         by the mod given
#     :param value: int: any number
#     :param mod: int: number to multiple value by
#     :return: bool: True or False
#     """
#     return (value % mod) == 0
#
#
# # RED PHASE 7 - Step 1 - failing test case
# def test_returns_fizzbuzz():
#     """
#     This test case will verify we get "fizzbuzz" when passing
#         in 15 as the argument
#     :return: bool: True or False
#     """
#     checkFizzBuzz(15, "FizzBuzz")   # Verifies output using helper function

###############################################################################


# Create a production code function
def fizzBuzz(value):
    """
    This function checks if the value is a multiple of 3, 5, or 3 and 5.
    :param value: int: any number
    :return: str: "Fizz" if multiple of 3
                  "Buzz" if multiple of 5
                  "FizzBuzz" if multiple of 3 and 5
                  "<value given>" if none apply
    """
    if isMultiple(value, 3):    # Is the value a multiple of 3?
        if isMultiple(value, 5):    # Is the value a multiple of 5 too?
            return "FizzBuzz"   # Return "FizzBuzz" if both are true
        return "Fizz"   # Return "Fizz" if only multiple of 3
    if isMultiple(value, 5):    # Is the value a multiple of 5 only?
        return "Buzz"   # Return "Buzz" if only multiple of 5
    return str(value)   # Otherwise, return the value as a string


def isMultiple(value, mod):
    """
    This function will verify if the value given can evenly be multiplied
        by the mod (the multiplier) given
    :param value: int: any number
    :param mod: int: number to multiple value by
    :return: bool: True or False
    """
    return (value % mod) == 0   # Returns True or False if can be multiplied


def checkFizzBuzz(value, expectedRetVal):
    """
    Helper function to check that values are being handled properly
        within the fizzBuzz function.
    :param value: int: any number
    :param expectedRetVal: str: the output expected
    :return: bool: True or False
    """
    retVal = fizzBuzz(value)    # The results of the function call
    assert retVal == expectedRetVal  # Assertion statement - verifies equality


def test_returns1With1PassedIn():
    """
    Function to test if we get "1" when passing in 1 as value argument
    :return: bool: True or False
    """
    checkFizzBuzz(1, "1")   # Verifies output using helper function


def test_returns2With2PassedIn():
    """
    Function to test if we get "2" when passing in 2 as value argument
    :return: bool: True or False
    """
    checkFizzBuzz(2, "2")   # Verifies output using helper function


def test_returnsFizzWith3PassedIn():
    """
    Function to test if we get "Fizz" when passing in 3 as value argument
    :return: bool: True or False
    """
    checkFizzBuzz(3, "Fizz")   # Verifies output using helper function


def test_returnsBuzzWith5PassedIn():
    """
    Function to test if we get "Buzz" when passing in 5 as value argument
    :return: bool: True or False
    """
    checkFizzBuzz(5, "Buzz")   # Verifies output using helper function


def test_returnsFizzWith6PassedIn():
    """
    Function to test if we get "Fizz" when passing in 6 as value argument
    :return: bool: True or False
    """
    checkFizzBuzz(6, "Fizz")   # Verifies output using helper function


def test_returnsBuzzWith10PassedIn():
    """
    Function to test if we get "Buzz" when passing in 10 as value argument
    :return: bool: True or False
    """
    checkFizzBuzz(10, "Buzz")   # Verifies output using helper function


def test_returnsFizzBuzzWith15PassedIn():
    """
    Function to test if we get "FizzBuzz" when passing in 15 as value argument
    :return: bool: True or False
    """
    checkFizzBuzz(15, "FizzBuzz")   # Verifies output using helper function
