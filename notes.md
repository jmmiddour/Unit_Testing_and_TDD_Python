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

### [Supermarket Checkout Kata overview](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/supermarket-checkout-kata-overview)

Overview of the Test Cases needing to implement:

- Can create an instance of the Checkout class

- Can add an item price

- Can add an item

- Can calculate the current total

- Can add multiple items and get correct total

- Can add discount rules

- Can apply discount rules to the total

- Exception is thrown for item added without a price

### [Setup and first test case](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/setup-and-first-test-case)

Created `TestCheckout.py` and `Checkout.py` and implemented the first test case of "Can create an instance of the Checkout class"

In the `TestCheckout.py`:

```
from Checkout import Checkout

def test_CanInstantiateCheckout():
    co = Checkout()
```

In the `Checkout.py`:

```
class Checkout:
    pass
```

### [Add items, add item prices, and calculate current total](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/add-items-add-items-prices-and-calculate-current-total)

Can add an item price:

```
# In the TestCheckout.py file
def test_CanAddItemPrice():
    co = Checkout()
    co.addItemPrice('a', 1)
    
# In the Checkout.py file under the `class Checkout`
def addItemPrice(self, item, price):
    pass
```

- Refactor phase: Removed the `test_CanInstantiateCheckout`, it is no longer needed.

Can add an item:

```
# In the TestCheckout.py file
def test_CanAddItem():
    co = Checkout()
    co.addItem('a')

# In the Checkout.py file under the `class Checkout`
def addItem(self, item):
    pass
```

- Refactor phase: Create a Test Fixture because we are repeating the instantiation of `Checkout()` in all tests.

  ```
  @pytest.fixture()
  def checkout():
      checkout = Checkout()
      return checkout
  
  # Change the test already added to use this fixture
  def test_CanAddItemPrice(checkout):
      checkout.addItemPrice('a', 1)
  
  def test_CanAddItem(checkout):
      checkout.addItem('a')
  ```

Can calculate the current total:

```
# In the TestCheckout.py file
def test_CanCalculateTotal(checkout):
    checkout.addItemPrice('a', 1)
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1

# In the Checkout.py file under the `class Checkout`
def calculateTotal(self):
    return 1
```

- Refactor phrase: Remove the `test_CanAddItemPrice` and `test_CanAddItem` as they are no longer needed because they are both being done in the `test_CanCalculateTotal`

### [Add multiple items and calculate total](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/add-multiple-items-and-calculate-total)

In the `TestCheckout.py`:

```
def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItem("a", 1)
    checkout.addItem("b", 2)
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3
```

In the `Checkout.py` under the `Checkout` class:

```
def __init__(self):
    # Create a dictionary to hold the item (key), price (value)
    self.prices = {}
    # Instantiate the total cost at 0
    self.total = 0
    
def addItemPrice(self, item, price):
    # add the item and price to the prices dictionary
    self.prices[item] = price
    
def addItem(self, item):
    self.total += self.prices[item]
    
def calculateTotal(self):
    return self.total
```

### [Add and apply discounts](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/add-and-apply-discounts)

Can add discount rules:

- In the `TestCheckout.py`:

  ```
  def test_canAddDiscountRule(checkout):
      checkout.addDiscount("a", 3, 2)
  ```

- In the `Checkout.py` under the `Checkout` class:

  ```
  def addDiscount(self, item, nbrOfItems, price):
      pass
  ```

- Refactor phase: The `addItemPrice` is repeated in multiple test, going to add this for both items a and b to the Test Fixture and remove them from the test they are in.

Can apply discount rules to the total:

- In the `TestCheckout.py`:

  ```
  def test_canApplyDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    assert checkout.calculateTotal() == 2
  ```

- In the `Checkout.py` under the `Checkout` class:

  ```
  class Discount:
      def __init__(self, nbrItems, price):
          self.nbrItems = nbrItems
          self.price = price

  def __init__(self):
      self.prices = {}
      self.discounts = {}
      self.items = {}

  def addDiscount(self, item, nbrOfItems, price):
      discount = self.Discount(nbrOfItems, price)
      self.discounts[item] = discount
  
  def addItem(self, item):
      if item in self.items:
          self.items[item] += 1
      else:
          self.items[item] = 1
  
  def calculateTotal(self):
      total = 0
  
      for item, cnt in self.items.items():
          if item in self.discounts:
              discount = self.discounts[item]
  
              if cnt >= discount.nbrItems:
                  nbrOfDiscounts = cnt/discount.nbrItems
                  total += nbrOfDiscounts * discount.price
                  remaining = cnt % discount.nbrItems
                  total += remaining * self.prices[item]
  
              else:
                  total += self.prices[item] * cnt
  
          else:
              total += self.calculateItemTotal(item, cnt)
  
      return total
  ```

- Refactor phase: 

  - The `addItemPrice` is repeated in multiple test, going to add this for both items a and b to the Test Fixture and remove them from the test they are in.
  
  - Create two new methods within the `Checkout` class to calculate the item total and the item discount total and this will also remove some code from the `calculateTotal` method:
  
    ```
    def calculate_item_total(self, item, cnt):
        """
        Class method to calculate the total after discounts
        :param item: str: single item from available items
        :param cnt: int: number of the given item
        :return: The total cost for the given item after discounts
        """
        total = 0

        # If given item has a discount available...
        if item in self.discounts:
            # Instantiate discounted price
            discount = self.discounts[item]

            # If the given count is >= the number of items need for the discount
            if cnt >= discount.num_items:
                # Total will be calculated based on discounted price
                total += self.calculate_item_discounted_total(item, cnt, discount)

            else:  # Otherwise...
                # Total will be calculated based on regular price
                total += self.prices[item] * cnt

        else:  # If item not in the discounts...
            # Total will be calculated based on regular price
            total += self.prices[item] * cnt

        return total
    
    def calculate_item_discounted_total(self, item, cnt, discount):
        """
        Class method to calculate the total of an item based on the
            discounted price and the number of that item
        :param item: str: single item from available items
        :param cnt: int: number of the given item
        :param discount: float: the discounted price of given item
        :return: float: the total after discount is applied
        """
        total = 0
        # How many of the item will get the discount price?
        num_of_discounts = cnt / discount.num_items
        # Total of discounted items
        total += num_of_discounts * discount.price
        # Total of remaining items that do not get the discount price
        remaining = cnt % discount.nbrItems
        # Complete total for the item given
        total += remaining * self.prices[item]
        return total
    ```

- **TIP:** If you need to skip a test while making changes to ensure that no other test fail while making the changes (i.e. when you need to do a lot of refactoring to existing code to make current test pass) you can use a mark decorator: `@pytesst.mark.skip`

- All code changes and additional comments are in the `Exercise_Files/code_samples/checkout_kata/Checkout.py` and `Exercise_Files/code_samples/checkout_kata/TestCheckout.py` files.

### [Throw exception when adding an item with no price](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/throw-exception-when-adding-an-item-with-no-price)

In the `TestCheckout.py`:

```
def test_exception_bad_item(checkout):
    """
    Test function to check the exception is being raised for a bad item
    :param checkout: Test Fixture
    :return: bool: Pass or Fail
    """
    with pytest.raises(Exception):
        checkout.add_item("c")
```

In the `Checkout.py` under the `Checkout` class, change `add_item` method:

```
def add_item(self, item):
    """
    Class method to add item count to the items dictionary
    :param item: str: single item from available items
    :return: add 1 to the count for the item to the items dictionary
    """
    # If the item is not a valid item...
    if item not in self.prices:
        # Raise an exception
        raise Exception("Bad Item")

    if item in self.items:      # If already in items...
        self.items[item] += 1   # Increment count by 1

    else:                       # Otherwise...
        self.items[item] = 1    # Add item as key with value of 1
```

## Test Doubles

### [Test doubles, `unittest.mock`, and `monkeypatch` overview](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/test-doubles-unittest-mock-and-monkeypatch-overview)

What is Test Doubles?

- Almost all code depends on (i.e. collaborates) with other parts of the system.

- Those other parts of the system are not always easy to replicate in the unit test environment or would make tests slow if used directly.

  - For example, if your code queries a third-party API and that server is down, you can't run your tests.

- Test doubles are the answer to that problem. They are objects that are used in unit tests as replacements to the real production system collaborators.

Types of Test Doubles:

- **Dummy:** These are the simplest. Objects (placeholders) that can be passed around as necessary but do not have any type of test implementation and should never be used. They will often generate exceptions when they are called.

- **Fake:** These objects are different and generally have a simplified implementation from the production collaborator that make them usable for the test code but not suitable for production.  

- **Stub:** These objects do expect to be called but do respond with canned answers that are suitable for the test.

- **Spies:** These objects provide implementation that records the values that were passed in, so the test can then use those values for validating the code on the test.

- **Mock:** These objects are the most sophisticated of all the test doubles. They have pre-programmed expectations about the ordering of calls, the number of times that functions will be called, and the parameters that will be passed in. Mock objects will generate their own exceptions when these pre-programmed expectations are not met.

Mock Frameworks:

- Libraries that provide easy to use APIs for automatically creating any of these types of test doubles ***at runtime***.

- They provide easy APIs for specifying the mocking expectations for your tests.

- They can be much more efficient than implementing your own custom mock objects.

- Creating your own mock objects can be time-consuming, tedious, and error prone.

`unittest.mock`

- A mocking framework built-in to Python 3.3 and newer.

- For older versions of Python, you can install it with the command `pip install mock`.

`unittest.mock` - Mock Class:

- The Mock class is an extremely powerful class which can be used to create test objects that can be used as a fake, stub, spy, or true mock for all your tests.

- The Mock class has many initialization parameters for controlling its behavior. Such as what interface it should mock, if it should call another function when it's called, or what value it should return.

- Once a Mock object has been used, it has many built-in functions for verifying how it was used. Such as how many times it was called, and with what parameters. 

- Example:

  ```
  def test_foo():
      bar = Mock()
      function_that_uses_bar(bar)
      bar.assert_called_once()
  ```
  
Mock - Initialization:

- Provides many initialization parameters which can be used to control the mock object's behavior.

- The `spec` parameter specifies the interface that the Mock object is implementing. If any attributes of the Mock object are called which are not in that interface, the mock will automatically generate an `AttributeException`.

- The `side_effect` parameter specifies a function that should be called when the mock is called. This can be useful for more complicated test logic that returns different values depending on input parameters or generates exceptions.

- The `return_value` parameter specifies the return value when the Mock object is called. If the `side_effect` value is set, its `return_value` is used instead.

- Example:

  ```
  def test_foo():
      bar = Mock(spec=SpecClass)
      bar2 = Mock(side_effect=bar_func)
      bar3 = Mock(return_value=1
  ```
  
Mock - Verification:

- Mock provides many built-in functions for verifying how it was called, including the following assert functions:

  - `assert_called` - Will pass if the Mock was ever called with any parameters.
  
  - `assert_called_once` - Will pass if the Mock was called exactly once.
  
  - `assert_called_with` - Will pass if the Mock was last called with specified parameters
  
  - `assert_called_once_with` - Will pass if the Mock was called exactly once with specified parameters
  
  - `assert_any_call` - Will pass if the Mock was every called with the specified parameters
  
  - `assert_not_called` - Will pass if the Mock was never called 
  
Mock - Additional Verification:

- Mock provides these additional built-in attributes for verification of how it was called:

  - `assert_has_calls` - Passes if the Mock was called with the parameters specified and each of the passed in list of mock call objects, and, optionally, in the order that those call objects are put into the list
  
  - `called` - A bool which is True id if the Mock was ever called
  
  - `call_count` - An integer value representing the number of times the mock object was called
  
  - `call_args` - Contains the parameters that the Mock object was last called with 
  
  - `call_args_list` - A list containing the arguments that were used for each call to the Mock object
  
`unittest.mock` - MagicMock Class

- This class is derived from Mock and provides a default implementation of many of the default "magic" (dunder) methods defined in Python (i.e. `__str__`)

- The following magic methods ***not*** supported by MagicMock: `__getattr__`, `__setattr__`, `__init__`, `__new__`, `__prepare__`, `__instancecheck__`, `__subclasscheck__`, and `__del__`

PyTest Monkeypatch Test Fixture:

- PyTest provides the `monkeypatch` test fixture to allow a test to dynamically change the following:

  - module and class attributes
  
  - dictionary entries
  
  - environment variables
  
- Example:

  ```
  def call_it():
      print('Hello World')
  
  def test_patch(monkeypatch):
      monkeypatch(call_it, Mock())
      call_it()
      call_it.assert_called_once()
  ```

### [Example: `unittest.mock`](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/example-unittest-mock)

Can call `read_from_file`:

- In the `Exercise_Files/code_samples/unittest.mock_examples/TestDoubles_test.py` file:

  ```
  from LineReader import read_from_file
  
  def test_can_call_read_from_file():
      read_from_file('blah')
  ```

- In the `Exercise_Files/code_samples/unittest.mock_examples/LineReader.py` file:

  ```
  def read_from_file(filename):
      pass
  ```

`read_from_file` returns correct string:

- In the `Exercise_Files/code_samples/unittest.mock_examples/TestDoubles_test.py` file:

  ```
  import pytest
  from unittest.mock import MagicMock
  
  def test_returns_correct_string(monkeypatch):
      # Instantiate MagicMock
      mock_file = MagicMock()
  
      # Read the line from the Mock file
      mock_file.readline = MagicMock(return_value='test line')
  
      # Open the Mock file
      mock_open = MagicMock(return_value=mock_file)
  
      # Set the attributes for opening the Mock file
      monkeypatch.setattr("builtins.open", mock_open)
  
      # Get the results from the function call
      result = read_from_file("blah")
  
      # Verify that the Mock parameter was only called once
      mock_open.assert_called_once_with("blah", "r")
  
      # Verify the expected output was returned
      assert result == "test line"
  ```

- In the `Exercise_Files/code_samples/unittest.mock_examples/LineReader.py` file:

  ```
  def read_from_file(filename):
      # Open the given file and read it in
      infile = open(filename, "r")
  
      # Read line in the given file
      line = infile.readline()
  
      # Return the line read in from given file
      return line
  ```
  
- Refactor phase: Remove the first test `test_can_call_read_from_file` because it is not needed anymore as we are not reading in a real file. We could keep it by adding the mocks to it but not necessary as the `test_returns_correct_string` is going to be checking that functionality anyways.
  
`read_from_file` throws exception when file doesn't exist:

- In the `Exercise_Files/code_samples/unittest.mock_examples/TestDoubles_test.py` file:

  ```
  from pytest import raises
  
  def test_throws_exception_bad_file(monkeypatch):
      # Instantiate MagicMock
      mock_file = MagicMock()
  
      # Read the line from the Mock file
      mock_file.readline = MagicMock(return_value='test line')
  
      # Open the Mock file
      mock_open = MagicMock(return_value=mock_file)
  
      # Set the attributes for opening the Mock file
      monkeypatch.setattr("builtins.open", mock_open)
  
      # Let the computer know the file is a Mock file and does not exist.
      mock_exists = MagicMock(return_value=False)
  
      # Set the attricutes for non-existing Mock file
      monkeypatch.setattr("os.path.exists", mock_exists)
  
      # Test that the exception is executing properly
      with raises(Exception):
          result = read_from_file("blah")
  ```

- In the `Exercise_Files/code_samples/unittest.mock_examples/LineReader.py` file, modify `read_from_file`:

  ```
  import os
  
  def read_from_file(filename):
      # Check if the file exists...
      if not os.path.exists(filename):
          # If it does not exist, throw error message defined
          raise Exception("Bad File")
  
      # Open the given file and read it in
      infile = open(filename, "r")
  
      # Read line in the given file
      line = infile.readline()
  
      # Return the line read in from given file
      return line
  ```
  
- Refactor phrase:

  - Create a Test Fixture to pass in to both test for repetitive code:
  
    ```
    @pytest.fixture()
    def mock_open(monkeypatch):
        # Instantiate MagicMock
        mock_file = MagicMock()
    
        # Read the line from the Mock file
        mock_file.readline = MagicMock(return_value='test line')
    
        # Open the Mock file
        mock_open = MagicMock(return_value=mock_file)
    
        # Set the attributes for opening the Mock file
        monkeypatch.setattr("builtins.open", mock_open)
    
        return mock_open
    ```
    
  - Refactor the code for `test_returns correct string`:
  
    ```
    def test_returns_correct_string(mock_open, monkeypatch):
        # Fools the computer into thinking the file exists
        mock_exists = MagicMock(return_value=True)
  
        # Set the attricutes for non-existing Mock file
        monkeypatch.setattr("os.path.exists", mock_exists)
    
        # Get the results from the function call
        result = read_from_file("blah")
    
        # Verify that the Mock parameter was only called once
        mock_open.assert_called_once_with("blah", "r")
    
        # Verify the expected output was returned
        assert result == "test line"
    ```
    
  - Refactor the code for `test_throws_exception_bad_file`:
  
    ```
    def test_throws_exception_bad_file(mock_open, monkeypatch):
        # Let the computer know the file is a Mock file and does not exist.
        mock_exists = MagicMock(return_value=False)
    
        # Set the attricutes for non-existing Mock file
        monkeypatch.setattr("os.path.exists", mock_exists)
    
        # Test that the exception is executing properly
        with raises(Exception):
            result = read_from_file("blah")
    ```

## Test-Driven Development Best Practices

### [TDD best practices](https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/tdd-best-practices)

Always Do the Next Simplest Test Case:

- This allows you to gradually increase the complexity of your code, refactoring as you go. This helps to keep your code clean and understandable.

- If you jump into the complex test cases too quickly, you will find yourself stuck writing a lot of functionality all at once. This breaks the short feedback cycle that we look for with TDD.

- Beyond just slowing you down, this can also lead to bad design decisions. You could miss some simple implements that come from the incremental approach.

Use Descriptive Test Names:

- Code is read 1000 times more than it's witten. Make it clear and readable!

- Unit tests are the best documentation for how your code works for developers that come after you. Make them easy to understand because if the developers can not understand what the tests are doing, the documentation part is lost.

- Test suites should name the class or function under test, and the test names should describe the functionality being tested.

Keep Test Fast:

- One of the biggest benefits of TDD is the fast feedback on how your changes have affected things. 

- This goes away if your unit tests take more than a few seconds to build and run.

- To help your test stay fast, try to:

  - Keep console output to a minimum. This slows things down and can clutter up the testing framework output.

  - Mock out any slow collaborators with test doubles that are faster.
  
Use Code Coverage Analysis Tools:

- Once you have implemented all your test cases, go back and run your unit test through a code coverage tool.

- It can be surprising some code you will miss. This can help you identify any test cases that you may have missed.

- You should have a goal of 100% code coverage in functions with real logic in them (i.e. not simple getters/setters).

Run your Tests Multiple Times and in Random Order:

- Running your tests many times will help ensure that you don't have any flaky tests that fail intermittently.

- Running your tests in random order ensures that your tests don't have any dependencies between each other.

- Use the `python-random-order` plugin to randomize the order that the tests are executed, and the `pytest-repeat` plugin to repeat one or more tests a specific number of times.

Use a Static Code Analysis Tool:

- Pylint is an excellent open source static code analysis tool that will find errors in your code that you may have missed in your testing.

- Pylint can verify your python code meets your team's coding standard (or the PEP8 standard by default).

- Pylint can also detect duplicate code and can generate UML diagrams from its analysis of the code.

## Conclusion

### [Summary]()


