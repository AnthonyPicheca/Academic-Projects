"""
CSCA08: Winter 2024 -- Assignment 1: Wacky's Restaurant

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

Do not submit this file. Any changes you make to this file will
not be considered during grading. Ensure that all your work is
submitted in the designated files as per the instructions.
"""

AVAILABLE_SEAT_SYMBOL = '_'
TAKEN_SEAT_SYMBOL = 'X'

ITEM_HAMBURGER = 'HAMBURGER'
ITEM_HOT_DOG = 'HOT DOG'
ITEM_FRIES = 'FRIES'
ITEM_SODA = 'SODA'

PRICE_HAMBURGER = 17.50
PRICE_HOT_DOG = 10.50
PRICE_FRIES = 7.50
PRICE_SODA = 2.00

# Combos consist of the item itself, a serving of fries, and a soda.
PRICE_COMBO_HAMBURGER = 26.00
PRICE_COMBO_HOT_DOG = 19.00

# A hamburger consists of a hamburger patty, lettuce, and a hamburger bun.
COST_HAMBURGER_PATTY = 2.50
COST_LETTUCE = 0.50
COST_HAMBURGER_BUN = 0.50

# A hot dog consists of a hot dog and a hot dog bun.
COST_HOT_DOG = 2.25
COST_HOT_DOG_BUN = 0.25

# Fries and sodas do not have ingredients other than themselves.
COST_FRIES = 3.00
COST_SODA = 1.00
