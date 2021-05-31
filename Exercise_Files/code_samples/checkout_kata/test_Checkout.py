import pytest
from Checkout import Checkout


@pytest.fixture()
def checkout():
    """
    Test Fixture to be ran when called by any tests in this module (file)
    :return: Test Fixture functionality
    """
    checkout = Checkout()
    checkout.add_item_price("a", 1)
    checkout.add_item_price("b", 2)
    return checkout


def test_calculate_total(checkout):
    """
    Test function to check the `calculate_total` function is working properly,
        with a single item added.
    :param checkout: Test Fixture
    :return: bool: Pass or Fail
    """
    checkout.add_item("a")
    assert checkout.calculate_total() == 1


def test_correct_total_multiple_items(checkout):
    """
    Test function to check the `calculate_total` function is working properly,
        with multiple items added.
    :param checkout: Test Fixture
    :return: bool: Pass or Fail
    """
    checkout.add_item("a")
    checkout.add_item("b")
    assert checkout.calculate_total() == 3


def test_add_discount_rule(checkout):
    """
    Test function to check the `add_discount` function is working properly
    :param checkout: Test Fixture
    :return: bool: Pass or Fail
    """
    checkout.add_discount("a", 3, 2)


def test_apply_discount_rule(checkout):
    """
    Test function to check the `calculate_total` function is working properly,
        with multiple items and discount applied.
    :param checkout: Test Fixture
    :return: bool: Pass or Fail
    """
    checkout.add_discount("a", 3, 2)
    checkout.add_item("a")
    checkout.add_item("a")
    checkout.add_item("a")
    assert checkout.calculate_total() == 2


def test_exception_bad_item(checkout):
    """
    Test function to check the exception is being raised for a bad item
    :param checkout: Test Fixture
    :return: bool: Pass or Fail
    """
    with pytest.raises(Exception):
        checkout.add_item("c")
