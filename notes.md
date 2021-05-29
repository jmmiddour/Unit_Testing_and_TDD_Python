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


### [What is test-driven development (TDD)?](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/what-is-test-driven-development-tdd)

- A process for writing code where the developer takes personal responsibility for the quality of their code.

- Unit tests are written *before* the production code.

- Don't write all the tests or production code at once.

    - You write one unit test for one test case, then you write the production code to make it pass the test.
    
- The tests and production code are both written together in small bits of functionality.

- This short cycle of writing the unit test and then writing the production code to make it pass, provides immediate feedback on the code. This feedback is one of the essential features of TDD.

What are some benefits of using TDD?

- Gives you the confidence to make changes in the code because you have to test before you begin and that verifies the code is working and will tell you if any of your changes have broken anything.

- Gives you immediate feedback.

- The test documents what the production code is supposed to do.

- A new developer looking at the code can use the unit test a source of documentation for understanding what the production code is doing.

- Writing the unit test first helps to drive good object-oriented design. As making individual classes and functions testable in isolation, drives the developer to break the dependencies and add interfaces rather than linking concrete implementations together directly. 

TDD Beginnings:

- TDD was created by Kent Beck in the mid 1990's as part of his work for the Chrysler Corporation where he also created the Extreme Programming software development process. 

- He wrote the first TDD unit testing frameworks in `Smalltalk` called `SUnit`.

- Then he collaborated with Erich Gamma to implement the first Java unit testing framework `JUnit`.

- `JUnit` has been the basis for many other xUnit testing frameworks written for other languages.

TDD Workflow phases: Red, Green, Refactor:

- **Red:** Write a failing unit test for the next bit of functionality that you want to implement in the production code.

- **Green:** Write just enough production code to make the failing test from the *Red* phase pass.

- **Refactor:** Clean up the unit test, and the production code to remove any duplication and make sure the code follows your team standards and best practices.

- Then you repeat the process above until the feature is complete.

Uncle Bob's 3 Laws of TDD: From the book "Clean Code: A Handbook of Agile Software Development"

- These laws ensure that you are following the TDD process.

- "You may not write any production code until you have written a failing unit test." This follows along with writing the unit test first. Seeing your new unit test fail, before writing the production code is a sign that the unit test has been implemented properly.

- "You may not write more of a unit test than is sufficient to fail, and not compiling is failing." This forces you to only write enough of a test for the next test case, and the next test case should always be the simplest test case.

- "You may not write more production code than is sufficient to pass the currently failing unit test." This keeps you from writing production code without any unit test to verify it. 

### [Example TDD session: The FizzBuzz Kata](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/example-tdd-session-the-fizzbuzz-kata)

For this example, we will be using the FizzBuzz code Kata.

- The name **Kata** comes from *Martial Arts* and means training exercises.

- **Code Kata:** Training exercises for programmers.

- Work and notes can be found in `Exercise_Files/code_samples/fizzbuzz_kata/FizzBuzzTest.py`

## Setting Up a Development Environment

### [Python virtual environments](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/python-virtual-environments)

What are Python Virtual Environments?

- By default, all python packages are installed to a single directory on the system. This can pose a problem if you are working on multiple project that have different versions of the same dependencies. You can not have both versions installed in an environment at the same time.

- Virtual environments solve this by creating isolated python environments that can be customized per project.

- Virtual environments are directories containing links to the system's python install and providing the sub-directories for installing additional python packages in that particular virtual environment.

- The PATH environment variable is updated to point to the virtual environment when that virtual environment is activated.

Setting up a Python Virtual Environment in Python 2.7

- Install the `virtualenv` utility via `pip install virtualenv`

- Create a new virtual environment with the command `virtualenv <name of virtualenv>`

- Activate your virtual environment by sourcing the activate script in the virtual environment's bin directory `source ./<name of virtualenv>/bin/activate` (on my machine it is `source <name of virtualenv>/Script/activate`)

- Deactivate your virtual environment with the `deactivate` command

- Delete your virtual environment by deleting its directory

Setting up a Python Virtual Environment in Python 3

- Python 3 comes with a virtual environment module built-in called `venv`

- Virtualenv can also be used with Python 3 but venv is what's recommended by the Python community as it is built-in to python 3, creates smaller virtual environments and is extendable to include additional plug-ins.

- The only difference with creating, activating, deactivating, or deleting virtual environments with `venv` vs `virtualenv` is the creation command.

- To create a virtual environment with `venv` you run the command `python3 -m venv <virtual env name>`

- All other command are the same as with the `virtualenv`

Setting up a Python Virtual Environment in Windows

- Use a bash shell in Windows and from that shell use the above instructions

- Follow the instructions on the [python.org](https://docs.python.org/3/tutorial/venv.html) website for running virtual environments directly from Windows normal command line window.

### [Set up pytest in PyCharm](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/set-up-pytest-in-pycharm)

If you created your virtual environment in a BASH terminal: 

- Open PyCharm and click on "Create New Project"

- Make sure on the left panel that "Pure Python" is selected

- For "Location" this will be the location on your local machine where your project will live, and the last directory will be your root directory for the project.

- For the "Interpreter" click the dropdown and look for the virtual environment that your created earlier, then click the dots on the right, "Add Local", locate the directory for the virtual environment, locate the "Scripts" directory within it, then click on the `python.exe` file.

If you already have the project open and created the virtual environment in the project directory:

- You can activate your virtual environment in your terminal

- Click on the bottom right where it says "Python 3.8" to configure your interpreter.

  - Click on "Add Interpreter"

  - Make sure that "Virtual Environment" is selected on the right panel
  
  - Click on "Existing Environment"
  
  - Click the `...` to the left of the path for the "Interpreter"
  
  - Find your virtual environment directory, then the "Scripts" directory within that directory
  
  - Click on `python.exe` and click okay
  
- Set up Configuration:

  - Click on the dropdown at the top to edit/add configuration
  
  - Add a new configuration using the `+` and select the `pytest` under the `python test` section
  
  - Under "Target" - "Script path" - add the path to the .py file you want to run the test on.
  
  - Select your "Interpreter" and click okay.
  
- Now you can just click on the "play" button and your test will automatically run.

Code and more notes can be found in `Exercise_Files/code_samples/pytest_test.py`

### [Set up pytest in Eclipse PyDev](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/set-up-pytest-in-eclipse-pydev)

No need to use this application at the moment, so no notes on this one but did watch the video.

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


