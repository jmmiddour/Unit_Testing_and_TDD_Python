# Unit Testing and Test Driven Development in Python

[Link to the Course on LinkedIn Learning](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/welcome)

## Overview of Test-Driven Development

### [What is unit testing?](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/what-is-unit-testing)

Why do we unit test?

- Software bugs hurt the business!

- Software testing catches the bugs before they get to the field.

- This is done systematically with a multi-layer approach where each layer of testing provides a safety net for catching bugs before they get to the field

There are several levels of testing:

- **Unit Testing:** The lowest level - test at the function level.

    - Validates individual functions in the production code.
    
    - Generally the most comprehensive test which should test all positive and negative test cases for a function.

- **Component Testing:** Testing at the library and compiled binary level.

    - Tests the external interfacing for individual components.
    
    - **Components:** A collection of the functions.
    
- **System Testing:** Tests the external interfaces of a system which is a collection of components or sub-systems.

- **Performance Testing:** Testing done at sub-system and system levels to verify timing and resource usages are acceptable.

Unit Testing Specifics:

- The first safety net for catching bugs before they get to the field.

- Tests individual functions and code.

- A test should be writen for each test case for a function (all positive and negative test cases).

- Groups of tests can be combined into test suites for better organization.

- Executes in the development environment rather than the production environment. This is important to ensure that you can run them easily and often.

- Execution of the tests should be implemented in an automated fashion. You should be able to click a button, and the unit test should be able to build and execute.

- Unit tests should run fast! Ideally the developer should be able to rerun the tests every 3-5 minutes. 

- A simple example using `pytest`:

    ```
    import pytest
    
    # Production code
    def str_len(the_str):
        return len(the_str)
    
    # A Unit Test
    def test_str_len():
        test_str = '1'               # Set up step = "dummy data"
        result = str_len(test_str)   # Action step = Calls the function
        assert result == 1           # Assert step = Validates the results
    ```


### [What is test-driven development?](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/what-is-test-driven-development-tdd)



### [Example TDD session: The FizzBuzz Kata]()



## Setting Up a Development Environment

### [Python virtual environments]()



### [Set up pytest in PyCharm]()



### [Set up pytest in Eclipse PyDev]()



## Pytest Overview

### [Overview of pytest]()



### [Test discovery]()



### [An xunit-style setup and teardown]()



### [Test fixtures]()



### [Assert statements and exceptions]()



### [Command line arguments: pytest]()



## The Supermarket Checkout Kata

### [Supermarket Checkout Kata overview]()



### [Setup and first test case]()



### [Add items, add item prices, and calculate current total]()



### [Add multiple items and calculate total]()



### [Add and apply discounts]()



### [Throw exception when adding an item with no price]()



## Test Doubles

### [Test doubles, `unittest.mock`, and `monkeypatch` overview]()



### [Example: `unittest.mock`]()



## Test-Driven Development Best Practices

### [TDD best practices]()



## Conclusion

### [Summary]()


