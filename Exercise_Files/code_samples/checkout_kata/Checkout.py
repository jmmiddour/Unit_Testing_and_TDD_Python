
class Checkout:
    """
    Checkout class for all items, prices, discounts, and total
    This class will be used like a shopping cart
    """
    class Discount:
        """
        Discount class to create the rules for the discounts
        """
        def __init__(self, num_items, price):
            # Instantiate variable for number of items needed for discount
            self.num_items = num_items
            # Instantiate variable for price of item
            self.price = price

    def __init__(self):
        # Create a dictionary to hold the item (key), price (value)
        self.prices = {}
        # Create a dictionary to hold the number of items (key), price (value)
        self.discounts = {}
        # Create a dictionary to hold the item (key), number of item (value)
        self.items = {}

    def add_discount(self, item, num_of_items, price):
        """
        Class method to add the discount to the item entered
        :param item: str: single item from available items
        :param num_of_items: int: number of items to be purchased
        :param price: float: new price after the discount
        :return: adds the discount to the discounts dictionary
        """
        discount = self.Discount(num_of_items, price)
        self.discounts[item] = discount

    def add_item_price(self, item, price):
        """
        Class method to add the item price for the item given
        :param item: str: single item from available items
        :param price: float: price of the item
        :return: adds the price for the item to the prices dictionary
        """
        self.prices[item] = price

    def add_item(self, item):
        """
        Class method to add item count to the items dictionary
        :param item: str: single item from available items
        :return: add 1 to the count for the item to the items dictionary
        """
        # If the item is not a valid item
        if item not in self.prices:
            # Raise an exception
            raise Exception("Bad Item")

        if item in self.items:      # If already in items...
            self.items[item] += 1   # Increment count by 1

        else:                       # Otherwise...
            self.items[item] = 1    # Add item as key with value of 1

    def calculate_total(self):
        """
        Class method to calculate the total of all items
        :return: The total of all items
        """
        total = 0

        for item, cnt in self.items.items():
            total += self.calculate_item_total(item, cnt)

        return total

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
        remaining = cnt % discount.num_items
        # Complete total for the item given
        total += remaining * self.prices[item]
        return total
