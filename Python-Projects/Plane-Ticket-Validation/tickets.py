"""CSCA08 Fall 2023 Assignment 1.

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020-2023 Jacqueline Smith and Anya Tafliovich.

"""

from constants import (YR, MON, DAY, DEP, ARR, ROW, SEAT, FFN,
                       WINDOW, AISLE, MIDDLE, SA, SB, SC, SD, SE, SF)


# We provide this function solution as an example of correct
# documentation, as well as a function that uses constants.
def get_year(ticket: str) -> str:
    """Return the year of ticket 'ticket'.

    Precondition: 'ticket' is in valid format

    >>> get_year('20230915YYZYEG12F')
    '2023'
    >>> get_year('20240915YYZYEG12F1236')
    '2024'
    """

    return ticket[YR:YR + 4]


# We provide this function solution as an example of correct
# documentation, as well as a function that uses other functions as
# helpers.
def get_date(ticket: str) -> str:
    """Return the date of ticket 'ticket' in YYYYMMDD format.

    Precondition: 'ticket' is in valid format

    >>> get_date('20230915YYZYEG12F')
    '20230915'
    >>> get_date('20240915YYZYEG12F1236')
    '20240915'
    """

    return get_year(ticket) + get_month(ticket) + get_day(ticket)


# We provide the docstring for this function to help you get started.
def get_month(ticket: str) -> str:
    """Return the month of ticket 'ticket'.

    Precondition: 'ticket' is in valid format

    >>> get_month('20230915YYZYEG12F')
    '09'
    >>> get_month('20241215YYZYEG12F1236')
    '12'
    """

    pass  # replace this line with your solution


# We provide the docstring for this function to help you get started.
def visits_airport(ticket: str, airport: str) -> bool:
    """Return True if and only if either departure or arrival airport on
    ticket 'ticket' is the same as 'airport'.

    Precondition: 'ticket' is a valid ticket.

    >>> visits_airport('20230915YYZYEG12F1236', 'YEG')
    True
    >>> visits_airport('20230915YEGYYZ12F1236', 'YEG')
    True
    >>> visits_airport('20230915YYZYEG12F1236', 'YVR')
    False

    """

    pass  # replace this line with your solution


# We provide the docstring for this function to help you get started.
def get_seat_type(ticket: str) -> str:
    """Return WINDOW, AISLE, or MIDDLE depending on the type of seat in
    ticket 'ticket'.

    Precondition: 'ticket' is a valid ticket.

    >>> get_seat_type('20230915YYZYEG12F1236')
    'window'
    >>> get_seat_type('20230915YYZYEG08B')
    'middle'
    >>> get_seat_type('20230915YYZYEG12C1236')
    'aisle'

    """

    pass  # replace this line with your solution


# We provide the docstring for this function to help you get started.
def is_valid_seat(ticket: str, first_row: int, last_row: int) -> bool:
    """Return True if and only if ticket 'ticket' has a valid seat. That
    is, if the seat row is between 'first_row' and 'last_row',
    inclusive, and the seat is SA, SB, SC, SD, SE, or SF.

    Precondition: 'ticket' is in valid format.

    >>> is_valid_seat('20230915YYZYEG12F1236', 1, 30)
    True
    >>> is_valid_seat('20230915YYZYEG42F1236', 1, 30)
    False
    >>> is_valid_seat('20230915YYZYEG21Q1236', 1, 30)
    False

    """

    pass  # replace this line with your solution


# We provide the docstring for this function to help you get started.
def adjacent(ticket1: str, ticket2: str) -> bool:
    """Return True if and only if the seats in tickets 'ticket1' and
    'ticket2' are adjacent (next to each other). Seats across an aisle
    are not considered to be adjacent.

    Precondition: 'ticket1' and 'ticket2' are valid tickets.

    >>> adjacent('20230915YYZYEG12D1236', '20230915YYZYEG12E1236')
    True
    >>> adjacent('20230915YYZYEG12B1236', '20230915YYZYEG12A1236')
    True
    >>> adjacent('20230915YYZYEG12C1236', '20230915YYZYEG12D1236')
    False
    >>> adjacent('20230915YYZYEG12A1236', '20230915YYZYEG11B1236')
    False
    """

    pass  # replace this line with your solution


# We provide this function for you to use as a helper.
def is_valid_ticket_format(ticket: str) -> bool:
    """Return True if and only if ticket 'ticket' is in valid format:

    - year is 4 digits
    - months is 2 digits
    - day is 2 digits
    - departure is 3 letters
    - arrival is 3 letters
    - row is 2 digits
    - seat is a characters
    - frequent flyer number is either empty or 4 digits, and
      it is the last record in 'ticket'

    >>> is_valid_ticket_format('20241020YYZYEG12C1236')
    True
    >>> is_valid_ticket_format('20241020YYZYEG12C12361236')
    False
    >>> is_valid_ticket_format('ABC41020YYZYEG12C1236')
    False
    """

    return (FFN == 17
            and (len(ticket) == 17
                 or len(ticket) == 21 and ticket[FFN:FFN + 4].isdigit())
            and ticket[YR:YR + 4].isdigit()
            and ticket[MON:MON + 2].isdigit()
            and ticket[DAY:DAY + 2].isdigit()
            and ticket[DEP:DEP + 3].isalpha()
            and ticket[ARR:ARR + 3].isalpha()
            and ticket[ROW:ROW + 2].isdigit()
            and ticket[SEAT].isalpha())


if __name__ == '__main__':
    import doctest
    doctest.testmod()
