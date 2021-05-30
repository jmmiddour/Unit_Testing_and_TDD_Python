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

### [Overview of pytest](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/overview-of-pytest)

What is PyTest?

- A python unit testing framework

- It provides the ability to create Tests, Test Modules, and Test Fixtures

- Uses the built-in Python assert statement which makes it much easier to use than another testing frameworks

- It has command line parameters to help filter which tests are executed and in what order

Creating a Test:

```
# Create a file named "test_some_function.py"
def test_some_function():
    assert 1 == 1
```

- Tests are python functions with `test_` at the beginning of the function name

- The tests then test production code by doing a verification of values using the standard python assert statement

- Similar tests can be grouped together by including them in the same module or class

- Can also run it from the command line with `pytest -v` the `-v` just means verbose and do not need it but shows more information about the test when using it. This can be run from the root directory as long as the test file is named properly, the pytest command will find it, even if you are not in that current directory.

  - Can also add `-s` which will allow you to see print statements in the console when the test gets ran.

### [Test discovery](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/test-discovery)

- Pytest will automatically discover tests when you execute based on a standard naming convention

- Test functions should start with `test_`

- Classes with tests in them should start with `Test` at the beginning of the class name and not have an `__init__` method

- The file names of test modules should start or end with `test` (i.e. `test_example.py` or `example_test.py`)

### [An xunit-style setup and teardown](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/an-xunit-style-setup-and-teardown)

`XUnit` style setup/teardown functions will execute code before and after:

- Test Modules

  - `def setup_module():`
  
  - `def teardown_module():`

- Test Functions

  - `def setup_function():`
  
  - `def teardown_function():`

- Test Classes

  - `def setup_class():`
  
  - `def teardown_class():`

- Test Methods in Test Classes

  - `def setup_method():`
  
  - `def teardown_method():`
  
Using these setup and teardown functions can help reduce code duplication by letting you specify the set up and tear down code once at each of the different levels as necessary, rather than repeating the code in each individual unit test. 

- See `Exercise_Files/code_samples/test_file.py` for code examples and more notes from line 1 - line 253

### [Test fixtures](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/test-fixtures)

- Test Fixtures allow for the re-use of setup and teardown code across tests by specifying functions that should be ran before the unit test runs.

- You specify that a function is a Test Fixture by adding a decorator `@pytest.fixture()` directly before the function.

- Individual unit test can specify which fixtures they want executed by passing the name of that fixture in as its argument.

  - Example:
  
    ```
    @pytest.fixture()
    def math():
      return Math()
    
    def test_add(math):
      assert math.add(1, 1) == 2
    ```
    
- You can also set the `autouse` parameter to `True` to automatically execute a fixture before each test.

- See coding examples and comments in the `Exercise_Files/code_samples/test_file.py` from line 254 - line 438

Test Fixture Teardown:

- Often there is also a teardown function that needs to be done after all test have been completed.

- Each test fixture can specify their own optional teardown code which is called after a fixture goes out of scope.

- There are 2 methods for specifying a teardown code. 
  
  - The "yield" keyword:
  
    - When the "yeild" keyword is used, the code after the yield is executed after the fixture goes out of scope.
  
    - The "yield" keyword is a replacement for the return keyword so any return values are also specified in the yield statement.
  
    - Example:
  
      ```
      @pytest.fixture()
      def setup():
          print('Setup!')
          yeild
          print('Teardown!')
      ```
    
  - The request-context object's "addfinalizer" method:

    - This method is a little more complicated but a little more capable than the yield statement.
  
    - With the `addfinalizer` method, one or more finalizer functions are added via the request-context's `addfinalizer` method.
  
    - This method allows for multiple finalization functions, whereas the yield method does not.
  
    - Example:
  
      ```
      @pytest.fixture()
      def setup(request):
          print('Setup!')
          def teardown:
              print('Teardown!')
          request.addfinalizer(teardown)
      ```
      
- More code examples and comments in the `Exercise_Files/code_samples/test_file.py` file from line 439 - line 511

Test Fixture Scopes:

- Test fixtures can have the following 4 different scopes which specify how often the fixture will be called:

  1. Function - (Default) Run the fixture once for each test defined in the module (file).
  
  2. Class - Run the fixture once for each class of tests.
  
  3. Module - Run once when the module (file) goes in scope. (when the file is called)
  
  4. Session - The fixture is run once when pytest starts
  
- See examples in `Exercise_Files/code_samples/test_file.py` line 512 - line 592 and `Exercise_Files/code_samples/test_file2.py` line 1 - line 79

Test Fixture Return Objects and Params

- Test fixtures can optionally return data which can be used in the test.

- The optional "params" array argument in the fixture decorator can be used to specify the data returned to the test.

- When the "params" argument is specified then the test will be called one time with each value specified.

- Example:

  ```
  @pytest.fixture(params=[1, 2])
  def setup_data(request):
      return request.param
  
  def test1(setup_data):
      print(setup_data)
  ```
  
- See more code examples in `Exercise_Files/code_samples/test_file.py` line 593 - line 641

### [Assert statements and exceptions](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/assert-statements-and-exceptions)

Using the `assert` Statement:

- Pytest allows the use of the built-in python assert statement for performing verifications in a unit test.

- The normal comparison operators, such as `<`, `>`, `<=`, `>=`, `==`, and `!=` can be used on all python data types.

- Pytest expands on the message returned from the assert failures to provide more context in the test results.

- Example:

  ```
  def test_int():  # Test for integer data type
      assert 1 == 1
  
  def test_str():  # Test for string data type
      assert 'str' == 'str'
  
  def test_float():  # Test for float data type
      assert 1.0 == 1.0
  
  def test_array():  # Test for array/list format
      assert [1, 2, 3] == [1, 2, 3]
  
  def test_dict():  # Test for dictionary format
      assert {'1': 1} == {'1': 1}
  ```
  
Comparing Floating Point Values

- Validating floating point values can sometimes be difficult as internally the value is stored as series of binary fractions (i.e. 1/3 is internally 0.333...)

- Because of this some floating point comparisons that would be expected to pass, will fail.

  - Example of a failing test:
  
    ```
    def test_bad_float_comp():
        assert (0.1 + 0.2) == 0.3
    ```

- The pytest "approx" function can be used to verify that two floating point values are "approximately" equivalent to each other with a default tolerance of `1e-6`

  - Example of how to write the above failing test to pass:
  
    ```
    def test_good_float_comp():
        val = 0.1 + 0.2
        assert val == approx(0.3)
    ```
    
Verifying Exceptions:

- In some test cases we want to verify that a function throws an exception under certain conditions. 

- Pytest provides the "raises" helper to perform this verification using the "with" keyword.

- When the "raises" helper is used, the unit test will fail if the specified exception is not thrown in the code block after the "raises" line. 

  - Example:
  
    ```
    def test_exception():
        with raises(ValueError):
            raise ValueError
    ```
    
- See code example and more notes in `Exercise_Files/code_samples/test_file1.py` line 1 - line 105

### [Command line arguments: pytest](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/command-line-arguments-pytest)

Specifying What Tests Should Run:

- By default, Pytest will automatically discover and run all tests in all properly named modules (files) from the current working directory and sub-directories.

- There are several command line arguments for controlling which discovered tests actually are executed.

  - moduleName - Simply specify the module name to run only the tests in that module (file).
  
  - DirectoryName/ - Runs any tests found in the specified directory.
  
  - `-k` expression - Matches tests found that match the evaluate expression in the string. The string values can include module, class, and function names (i.e. "TestClass and TestFunction").
  
  - `-m` expression - Matches tests found that have a "pytest mark" decorator that matches the specified expression.
  
Additional Useful Command Line Arguments:

- `-v` Report in verbose mode

- `-q` Run in quiet mode (Can be helpful when running hundreds or thousands of tests at once).

- `-s` Don't capture the console output (shows print statements on the console).

- `--ignore` Ignore the specified path when discovering tests.

- `--maxfail` Stop after the specified number of failures.

- Some Examples:

  - `pytest -v -s` will run all tests discovered in the current working directory and any sub-directories.
  
  - `pytest -v -s <file name in cwd>` will only run the tests in that file within the current working directory.
  
  - `pytest -v -s <sub-directory name>/` will only run the tests that are in the files in that directory.
  
  - `pytest -v -s -k "<test name>"` will only run the test specified in the string.
  
  - `pytest -v -s -k "<test name> or <test name>"` will run both of the test specified with the `or` separator.
  
  - `pytest -v -s -m "<name of mark test> or <name of mark test>"` will run only the test with the `mark` decorator and those test names (example: `@pytest.mark.<test name>`)
  
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


