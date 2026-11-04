####################################################################
# NOTE: Do not submit this file. No I/O is allowed in encryption.py.
####################################################################

from encryption import (
    is_valid_matrix,
    combine_rows,
    invert_binary_values,
    convert_binary_to_str,
    convert_str_to_binary,
    encrypt_or_decrypt,
    rotate_matrix,
    flip_matrix,
    solve_mystery_phrase,
)

from letters import LETTERS

import constants
from copy import deepcopy
from typing import TypeVar

Element = TypeVar("Element", int, str)

def print_matrix(matrix: list[list[Element]], pretty: bool = True) -> None:
    """Print the matrix!"""
    for row in matrix:
        if pretty:
            print("".join("*" if val else " " for val in row))
        else:
            print("".join(str(val) for val in row))


def user_input_for_print(msg: list[list[Element]]) -> None:
    """Ask user whether they want to print the matrix
    nicely or not, then print the matrix.
    """
    correctly_selected = False
    while not correctly_selected:
        mode = input("Pretty? (binary only) (y/n): ")
        if mode in {"y", "n"}:
            correctly_selected = True
    print_matrix(msg, True if mode == "y" else False)


def append_letter(msg: list[list[Element]]) -> list[list[Element]]:
    """Return the updated msg with the letter specified
    by the user appended to it.
    """

    selecting = True
    while selecting:
        letter = input("Please select a letter: ")
        try:
            letter_matrix = LETTERS[letter.upper()]
            if len(msg) == 0:
                msg = deepcopy(letter_matrix)
            else:
                combine_rows(msg, letter_matrix)
            selecting = False
        except:
            print("Not a valid letter, please select another...")

    return msg


def encrypt_msg(msg: list[list[Element]], encrypt: bool = True) -> list[list[Element]]:
    """Return the encrypted message specified by the user."""

    encrypting = True
    while encrypting:
        print("\n")
        mode = input(
            f"Convert to {'Str' if encrypt else 'Int'}: 0\n"
            "Rotate 90 degrees: 1\n"
            "Flip: 2\n"
            f"Shift {'Encryption' if encrypt else 'Decryption'}: 3\n"
            "View Message: 4\n"
            "Finished: 5\n"
            f"Please Select an {'Encryption' if encrypt else 'Decryption'} Mode: "
        )

        try:
            mode = int(mode)
        except:
            print("Not valid mode...")

        if mode == 0:
            if encrypt:
                convert_binary_to_str(msg)
            else:
                convert_str_to_binary(msg)
        elif mode == 1:

            selecting = True
            while selecting:
                num_rotations = input(
                    "How many 90 degree rotations would you like to perform? "
                )
                try:
                    if isinstance(int(num_rotations), int):
                        selecting = False
                except:
                    print("Invalid input, please select and integer...")

            for _ in range(int(num_rotations)):
                msg = rotate_matrix(msg)

        elif mode == 2:
            selecting = True
            while selecting:
                dir = input("Direction (h/v): ")
                if dir in {"h", "v"}:
                    selecting = False
                else:
                    print("Invalid input, please select h or v...")
            msg = flip_matrix(msg, True if dir == "h" else False)
        elif mode == 3:
            key = input("Please select an integer value as a key: ")
            try:
                key = int(key)
                encrypt_or_decrypt(msg, key, encrypt=encrypt)
            except:
                print(
                    "Either you did not convert to str, key is not an int, is too large or encrypt_or_decrypt is not implemented..."
                )
        elif mode == 4:
            user_input_for_print(msg)
        elif mode == 5:
            encrypting = False
        else:
            print("Not a valid mode...")

    return msg


def start_secret_message_solver() -> None:
    """Start secret message solver!"""
    encrypted = deepcopy(constants.SECRET_MESSAGE_ENCRYPTED)
    hashes = deepcopy(constants.SECRET_MESSAGE_HASH)
    for i in range(len(encrypted)):
        word = solve_mystery_phrase(encrypted[i], hashes[i], max_key_value=20)
        if len(word) == 0:
            print(
                f"Could not find key word {i+1}. Please check your solve_mystery_phrase function"
            )
        print_matrix(word)


def user_playing(player1_msg, player2_msg, player1=True):
    """Play the messaging game"""
    playing = True
    has_quit = False
    while playing:
        print("\n")
        mode = input(
            "Append Letter: 0\n"
            "View Message: 1\n"
            "Encrypt Message: 2\n"
            "Invert Binary Values: 3\n"
            "Send Message: 4\n"
            "View Inbox: 5\n"
            "Decrypt Inbox: 6\n"
            "Solve Mystery Message: 7\n"
            "Quit: 8\n"
            f"Hello {'User 1 (Alice)' if player1 else 'User 2 (Bob)'}, please select a mode: "
        )
        try:
            mode = int(mode)
        except:
            print("Not valid mode...")

        if mode == 0:
            player1_msg = append_letter(player1_msg)
        elif mode == 1:
            user_input_for_print(player1_msg)
        elif mode == 2:
            player1_msg = encrypt_msg(player1_msg)
        elif mode == 3:
            currently_selected = False
            while not currently_selected:
                invert_mode = input("Invert (msg|inbox): ")
                if invert_mode in {"msg", "inbox"}:
                    currently_selected = True
            invert_binary_values(player1_msg 
                                 if invert_mode == "msg" else
                                 player2_msg)
        elif mode == 4:
            playing = False
        elif mode == 5:
            user_input_for_print(player2_msg)
        elif mode == 6:
            encrypt_msg(player2_msg, False)
        elif mode == 7:
            start_secret_message_solver()
        elif mode == 8:
            has_quit = True
            playing = False
        else:
            print("Not a valid mode...")

    return player1_msg, player2_msg, has_quit


def begin_communication() -> None:
    """Initialize the messaging platform!"""
    has_quit = False
    alice_msg = []
    bob_msg = []
    while not has_quit:
        alice_msg, bob_msg, has_quit = user_playing([], bob_msg)

        if has_quit:
            break
        print("\n\n\n")

        bob_msg, alice_msg, has_quit = user_playing([], alice_msg, player1=False)


############################# The Program: #############################
if __name__ == "__main__":

    import doctest

    doctest.testmod()
    import os

    constants.TESTING = False
    begin_communication()
