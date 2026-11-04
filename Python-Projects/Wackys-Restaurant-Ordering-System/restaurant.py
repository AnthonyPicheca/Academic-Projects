"""
CSCA08: Winter 2024 -- Assignment 1: Wacky's Restaurant

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.
"""

from constants import (AVAILABLE_SEAT_SYMBOL, TAKEN_SEAT_SYMBOL,
                       ITEM_HAMBURGER, ITEM_HOT_DOG, ITEM_FRIES, ITEM_SODA,
                       PRICE_HAMBURGER, PRICE_HOT_DOG, PRICE_FRIES, PRICE_SODA,
                       PRICE_COMBO_HAMBURGER, PRICE_COMBO_HOT_DOG,
                       COST_HAMBURGER_PATTY, COST_LETTUCE, COST_HAMBURGER_BUN,
                       COST_HOT_DOG, COST_HOT_DOG_BUN, COST_FRIES, COST_SODA)


def seat_customers(seats: str, count: int) -> str:
    """Given the initial seating arrangement 'seats', return the new seating
    arrangement after a number of customers 'count' have been seated.

    Customers must be seated with the seats closest to the beginning of the
    string. If there are not enough seats for the given number of customers,
    return "NOT POSSIBLE" instead.

    Preconditions: count >= 1
                   The seating arrangement 'seats' only contains either
                   AVAILABLE_SEAT_SYMBOL or TAKEN_SEAT_SYMBOL.

    >>> seat_customers('___XX_', 2)
    'XX_XX_'
    >>> seat_customers('X_X_X_X_X', 3)
    'XXXXXXX_X'
    >>> seat_customers('X_X', 100)
    'NOT POSSIBLE'

    """
    if (len(seats) < count) or (seats.count(AVAILABLE_SEAT_SYMBOL) < count):
        return "NOT POSSIBLE"
    return seats.replace(AVAILABLE_SEAT_SYMBOL, TAKEN_SEAT_SYMBOL, count)

def seat_customers_together(seats: str, group_size: int) -> str:
    """Customers typically arrive in groups of size 'group_size'. Given the
    initial seating arrangement 'seats', return the new seating arrangement
    after the group of customers have been seated together.

    Groups must be seated sequentially, with the seats closest to the beginning
    of the string. If it is not possible to seat the group sequentially,
    return "NOT POSSIBLE" instead.

    Preconditions: group_size >= 1
                   The seating arrangement 'seats' only contains either
                   AVAILABLE_SEAT_SYMBOL or TAKEN_SEAT_SYMBOL.

    >>> seat_customers_together('__XXX_', 2)
    'XXXXX_'
    >>> seat_customers_together('X__X__', 2)
    'XXXX__'
    >>> seat_customers_together('X_X_X_X_X', 2)
    'NOT POSSIBLE'

    """
    index = seats.find (AVAILABLE_SEAT_SYMBOL * group_size)
    if not index == -1:
        return (seats[:index] + TAKEN_SEAT_SYMBOL * group_size +
                seats[index + group_size:])
    return "NOT POSSIBLE"

def seat_customers_together_at_location(seats: str, group_size: int,
                                        starting_location: int) -> str:
    """Customers typically arrive in groups of size 'group_size'. Furthermore,
    they sometimes also want to pick where they want to sit. Given the
    initial seating arrangement 'seats', return the new seating arrangement
    after the group of customers have been seated together, starting at the
    given index of the string 'starting_location'.

    Groups must be seated sequentially. If it is not possible to seat the group
    sequentially at the requested position, return "NOT POSSIBLE" instead.

    Preconditions: group_size >= 1
                   len(seats) > starting_location >= 0
                   The seating arrangement 'seats' only contains either
                   AVAILABLE_SEAT_SYMBOL or TAKEN_SEAT_SYMBOL.

    >>> seat_customers_together_at_location('XX______XX', 2, 4)
    'XX__XX__XX'
    >>> seat_customers_together_at_location('XX____', 2, 4)
    'XX__XX'
    >>> seat_customers_together_at_location('XX__XX', 2, 1)
    'NOT POSSIBLE'
    >>> seat_customers_together_at_location('XX__XX', 2, 3)
    'NOT POSSIBLE'
    >>> seat_customers_together_at_location('XX____', 2, 5)
    'NOT POSSIBLE'

    """

    are_seats_available = (seats.find((AVAILABLE_SEAT_SYMBOL * group_size),
                            starting_location, starting_location+group_size))
    if are_seats_available == -1:
        return "NOT POSSIBLE"
    new_seats = (seats[:are_seats_available] + TAKEN_SEAT_SYMBOL * group_size
                 + seats[are_seats_available + group_size:])
    return new_seats

def clean_seats(seats: str, count: int) -> str:
    """Given the initial seating arrangement 'seats', return the new seating
    arrangement after cleaning up a given number of seats 'count'.

    Seats are cleaned starting from the seats closest to the beginning of the
    string. If there are not enough taken seats to clean, return
    "NOT POSSIBLE" instead.

    Preconditions: count >= 0

    >>> clean_seats('XX_XX_', 2)
    '___XX_'
    >>> clean_seats('X_X_X_X_X', 3)
    '______X_X'
    >>> clean_seats('X_X', 100)
    'NOT POSSIBLE'

    """
    if(len(seats) < count) or (seats.count(AVAILABLE_SEAT_SYMBOL) < count):
        return "NOT POSSIBLE"
    return seats.replace(TAKEN_SEAT_SYMBOL, AVAILABLE_SEAT_SYMBOL, count)

def is_valid_item(item_name: str) -> bool:
    """Return True if and only if the given name of an item 'item_name'
    represents a valid item sold by the restaurant.

    Valid items are defined by the constants ITEM_HAMBURGER, ITEM_HOT_DOG,
    ITEM_FRIES, and ITEM_SODA.

    >>> is_valid_item('HAMBURGER')
    True
    >>> is_valid_item('WATER')
    False

    """
    return item_name in {ITEM_HAMBURGER, ITEM_HOT_DOG, ITEM_FRIES, ITEM_SODA}

def can_be_combo(item_name: str) -> bool:
    """Return True if and only if the given name of an item 'item_name'
    represents a valid combo item sold by the restaurant.

    Valid combo items are defined by the constants ITEM_HAMBURGER and
    ITEM_HOT_DOG.

    >>> can_be_combo('HAMBURGER')
    True
    >>> can_be_combo('FRIES')
    False

    """
    return item_name in {ITEM_HAMBURGER, ITEM_HOT_DOG}

def calculate_item_price(item_name: str, amount: int) -> float:
    """Calculate and return the total price based on a given item's name
    'item_name' and the quantity 'amount'.

    Each valid item has a corresponding constant denoting its unit price.
    Valid item names are calculated using the function 'is_valid_item'.
    If the given item is not valid or the given quantity is less than 0,
    return 0.0 instead.

    >>> calculate_item_price('HAMBURGER', 3)
    52.5
    >>> calculate_item_price('WATER', -3)
    0.0

    """
    if item_name == 'HAMBURGER':
        return PRICE_HAMBURGER * amount
    if item_name == 'HOT DOG':
        return PRICE_HOT_DOG * amount
    if item_name == 'FRIES':
        return PRICE_FRIES * amount
    if item_name == 'SODA':
        return PRICE_SODA * amount
    return 0.0

def calculate_item_cost(item_name: str, amount: int) -> float:
    """Calculate and return the total cost based on a given item's name
    'item_name' and the quantity 'amount'.

    Each valid item has an individual list of ingredients, each with its own
    corresponding cost constant. The unit cost of a product is the sum of the
    costs of all its ingredients. Valid item names are calculated using the
    function 'is_valid_item'. If the given item is not valid or the given
    quantity is less than 0, return 0.0 instead.

    >>> calculate_item_cost('HAMBURGER', 3)
    10.5
    >>> calculate_item_cost('WATER', -3)
    0.0

    """
    if item_name == 'HAMBURGER':
        return ((COST_HAMBURGER_PATTY + COST_LETTUCE +
                 COST_HAMBURGER_BUN) * amount)
    if item_name == 'HOT DOG':
        return (COST_HOT_DOG + COST_HOT_DOG_BUN) * amount
    if item_name == 'FRIES':
        return (COST_FRIES) * amount
    if item_name == 'SODA':
        return (COST_SODA) * amount
    return 0.0

def calculate_item_profit(item_name: str, amount: int) -> float:
    """Calculate and return the total profit based on a given item's name
    'item_name' and the quantity 'amount'.

    The profit is determined as the customer's paying price (calculated using
    'calculate_item_price') minus the restaurant's ingredients cost (calculated
    using 'calculate_item_cost'). Valid item names are calculated using the
    function 'is_valid_item'. If the given item is not valid or the given
    quantity is less than 0, return 0.0 instead.

    >>> calculate_item_profit('HAMBURGER', 3)
    42.0
    >>> calculate_item_profit('WATER', -3)
    0.0

    """
    if item_name == 'HAMBURGER':
        return (((PRICE_HAMBURGER) - (COST_HAMBURGER_PATTY + COST_LETTUCE +
                                      COST_HAMBURGER_BUN)) * amount)
    if item_name == 'HOT DOG':
        return ((PRICE_HOT_DOG) - (COST_HOT_DOG + COST_HOT_DOG_BUN)) * amount
    if item_name == 'FRIES':
        return (PRICE_FRIES - COST_FRIES) * amount
    if item_name == 'SODA':
        return (PRICE_SODA - COST_SODA) * amount
    return 0.0

def calculate_combo_price(combo_item_name: str, amount: int) -> float:
    """Calculate and return the total price based on a given combo item's
    name 'combo_item_name' and the quantity 'amount'.

    Each valid combo item has a corresponding constant denoting its unit price.
    Valid combo item names are calculated using the function 'can_be_combo'.
    If the given item is not a valid combo item or the given quantity is less
    than 0, return 0.0 instead.

    >>> calculate_combo_price('HAMBURGER', 3)
    78.0
    >>> calculate_combo_price('PIZZA', -3)
    0.0

    """
    if combo_item_name == 'HOT DOG':
        return PRICE_COMBO_HOT_DOG * amount
    if combo_item_name == 'HAMBURGER':
        return PRICE_COMBO_HAMBURGER * amount
    return 0.0

def calculate_combo_cost(combo_item_name: str, amount: int) -> float:
    """Calculate and return the total cost based on a given combo item's
    name 'combo_item_name' and the quantity 'amount'.

    A combo order consists of the primary item 'combo_item_name', ITEM_FRIES,
    and ITEM_SODA. Each valid item has an individual list of ingredients, each
    with its own corresponding cost constant. The unit cost of a combo is the
    sum of the costs of all its ingredients. Valid combo item names are
    calculated using the function 'can_be_combo'. If the given item is not a
    valid combo item or the given quantity is less than 0, return 0.0 instead.

    >>> calculate_combo_cost('HAMBURGER', 3)
    22.5
    >>> calculate_combo_cost('PIZZA', -3)
    0.0

    """
    if combo_item_name == 'HOT_DOG':
        return ((COST_HOT_DOG + COST_HOT_DOG_BUN + COST_FRIES + COST_SODA)
                * amount)
    if combo_item_name == 'HAMBURGER':
        return ((COST_HAMBURGER_PATTY + COST_HAMBURGER_BUN + COST_LETTUCE +
                 COST_FRIES + COST_SODA) * amount)
    return 0.0

def calculate_combo_profit(combo_item_name: str, amount: int) -> float:
    """Calculate and return the total profit based on a given combo item's
    name 'combo_item_name' and the quantity 'amount'.

    The profit is determined as the customer's paying price (calculated using
    'calculate_combo_price') minus the restaurant's ingredients cost
    (calculated using 'calculate_combo_cost'). Valid combo item names are
    calculated using the function 'can_be_combo'. If the given item is not a
    valid combo item or the given quantity is less than 0, return 0.0 instead.

    >>> calculate_combo_profit('HAMBURGER', 3)
    55.5
    >>> calculate_combo_profit('PIZZA', -3)
    0.0

    """
    if combo_item_name == 'HOT_DOG':
        return (((PRICE_COMBO_HOT_DOG) - (COST_HOT_DOG + COST_HOT_DOG_BUN +
                                          COST_FRIES + COST_SODA)) * amount)
    if combo_item_name == 'HAMBURGER':
        return (((PRICE_COMBO_HAMBURGER) - (COST_HAMBURGER_PATTY +
                                            COST_HAMBURGER_BUN + COST_LETTUCE +
                                            COST_FRIES + COST_SODA)) * amount)
    return 0.0

def get_item_from_sentence(customer_sentence: str) -> str:
    """Extract and return the name of the item the customer is ordering from
    their request sentence 'customer_sentence'.

    Customers will only order from the menu using one of the following phrases:
      - "Please give me a[ combo of] <item>."
      - "Can I have a <item>[ combo]?"

    In the phrases listed above:
      - '<item>' represents the name of the item.
      - '[ combo of]' and '[ combo]' are not required and may not be said.

    Return the name of the item found in the customer's request (eg. "FRIES").
    If the customer orders a combo, also return the string "COMBO" at the start
    of the string, seperate by a space (eg. "COMBO HAMBUGER"). If the
    customer's request is unclear or the item name or combo item is invalid,
    return "UNKNOWN" instead.

    >>> get_item_from_sentence("Please give me a FRIES.")
    'FRIES'
    >>> get_item_from_sentence("Can I have a HAMBURGER combo?")
    'COMBO HAMBURGER'
    >>> get_item_from_sentence("Please give me a WATER.")
    'UNKNOWN'
    >>> get_item_from_sentence("Where is the washroom?")
    'UNKNOWN'

    """
    is_combo = ""


    if "combo" in customer_sentence:
        is_combo = "COMBO"
    if "HAMBURGER" in customer_sentence:
        return is_combo + " HAMBURGER"
    if "HOT DOG" in customer_sentence:
        return is_combo + "HOT DOG"
    if "FRIES" in customer_sentence:
        return is_combo + "FRIES"
    if "SODA" in customer_sentence:
        return is_combo + "SODA"
    return "UNKNOWN"



if __name__ == '__main__':
    import doctest
    doctest.testmod()
