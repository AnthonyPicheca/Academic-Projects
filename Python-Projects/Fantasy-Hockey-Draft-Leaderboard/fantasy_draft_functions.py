"""CSCA08: Fall 2025 -- Assignment 1: Ice Hockey Fantasy Draft

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020-2025 Mario Badr, Jennifer Campbell, Tom Fairgrieve,
Diane Horton, Michael Liut, Jacqueline Smith, and Anya Tafliovich.

"""

from constants import (
    POINTS_PER_GOAL,
    POINTS_PER_ASSIST,
    POINTS_PER_HIT,
    F_DCS_PER_POINT,
    D_DCS_PER_POINT,
    FORWARDS_NEEDED,
    DEFENCEMEN_NEEDED,
    GOALIES_NEEDED,
    BUDGET,
    PLAYERS_TO_SELECT,
    FORWARD,
    DEFENCEMEN,
    GOALIE,
    SV_VALUE,
    GAA_VALUE,
)


# provided
def get_player_id(player: str) -> str:
    """Return the id of player if the string is non-empty;
    otherwise return the empty string.

    Precondition: player is the string of player stats as
    seen in players.txt or the empty string

    >>> get_player_id('MGO_PD_G0-_A14_DC43_H70_Pr5-')
    'MGO'
    >>> get_player_id('NSH_PF_G7-_A14_DC20_H73_Pr10')
    'NSH'
    >>> get_player_id('')
    ''

    """

    return player[:3]


# provided as example of calling another function as helper
def is_player_available(player: str, players_available: str) -> bool:
    """Return True if and only if the id of player is in players_available.

    Precondition: player is the string of player stats
                  as seen in players.txt or the empty string,
                  players_available is the string of player ids
                  that are currently available for selection seperated
                  by _.

    >>> is_player_available('MGO_PD_G0-_A14_DC43_H70_Pr5-', 'DOL_NCA_MGO_AHS_')
    True
    >>> is_player_available('GGG_PD_G0-_A14_DC43_H70_Pr5-', 'DOL_NCA_MGO_AHS_')
    False
    >>> is_player_available('', 'DOL_NCA_MGO_AHS_')
    False

    """

    if len(player) == 0:
        return False
    return get_player_id(player) in players_available


# provided
def get_position(player: str) -> str:
    """Return the position of player if player is non-empty;
    otherwise return the empty string.

    Precondition: player is the string of player stats
    as seen in players.txt or the empty string

    >>> get_position('MGO_PD_G0-_A14_DC43_H70_Pr5-')
    'D'
    >>> get_position('NSH_PF_G7-_A14_DC20_H73_Pr10')
    'F'
    >>> get_position('CLA_PG_GAA2.23_SV0.910_Pr20')
    'G'
    >>> get_position('')
    ''

    """

    if len(player) == 0:
        return ""
    return player[5]


def get_price(player: str) -> int:
    """Return the price of the player if player is non-empty;
    otherwise returns 0.

    Precondition: player is the string of player stats as
    seen in players.txt or the empty string. Price is either a two digit
    integer or a one digit integer followed by "-".

    >>> get_price('MGO_PD_G0-_A14_DC43_H70_Pr5-')
    5
    >>> get_price('NSH_PF_G7-_A14_DC20_H73_Pr10')
    10
    >>> get_price('CLA_PG_GAA2.23_SV0.910_Pr20')
    20
    >>> get_price('')
    0
    """

    if len(player) == 0:
        return 0
    price = player[-2:]
    return int(price.rstrip("-"))


def can_select(player: str, forwards_drafted: int, defencemen_drafted:
               int, goalies_drafted: int) -> bool:
    """Return True if player can be added without causing forwards_drafted,
    defencemen_drafted or goalies_drafted to exceed their respective maximums
    as listed in constants.py.

    Precondition: player is the string of player stats as
    seen in players.txt or the empty string

    >>> can_select('MGO_PD_G0-_A14_DC43_H70_Pr5-', 3, 2, 0)
    False
    >>> can_select('NSH_PF_G7-_A14_DC20_H73_Pr10', 3, 0, 0)
    False
    >>> can_select('CLA_PG_GAA2.23_SV0.910_Pr20', 3, 2, 0)
    True
    >>> can_select('', 3, 1, 1)
    True
    """

    if len(player) == 0:
        return True

    player_position = get_position(player)

    if player_position == 'F':
        return forwards_drafted + 1 <= FORWARDS_NEEDED

    if player_position == 'D':
        return defencemen_drafted + 1 <= DEFENCEMEN_NEEDED

    if player_position == 'G':
        return goalies_drafted + 1 <= GOALIES_NEEDED

    return False


def can_afford(budget: int, player: str) -> bool:
    """Returns True if player can be added to roster without turning budget
    into a negative value. Return True if player is the empty string.

    Precondition: player is the string of player stats as
    seen in players.txt or the empty string

    >>> can_afford(5, 'MGO_PD_G0-_A14_DC43_H70_Pr5-')
    True
    >>> can_afford(15, 'NSH_PF_G7-_A14_DC20_H73_Pr10')
    True
    >>> can_afford(15, 'CLA_PG_GAA2.23_SV0.910_Pr20')
    False
    >>> can_afford(99, '')
    True
    """

    return budget - get_price(player) >= 0


def update_budget(budget: int, player: str) -> int:
    """Return GM's new budget after adding player to the roster. If the player
    price is greater than the budget, a negative value is returned expressing
    how much over budget the GM has gone.

    Precondition: player is the string of player stats as
    seen in players.txt or the empty string

    >>> update_budget(100, 'MGO_PD_G0-_A14_DC43_H70_Pr5-')
    95
    >>> update_budget(15, 'NSH_PF_G7-_A14_DC20_H73_Pr10')
    5
    >>> update_budget(15, 'CLA_PG_GAA2.23_SV0.910_Pr20')
    -5
    >>> update_budget(99, '')
    99
    """

    return budget - get_price(player)


def add_to_team(player: str, roster: str) -> str:
    """Returns an updated version of roster with player's ID being added to the
    lineup. Players on the roster are seperated by an underscore. Players will
    not be added to the roster if they are already on the roster.

    Precondition: player is the string of player stats as
    seen in players.txt or the empty string

    >>> add_to_team('MGO_PD_G0-_A14_DC43_H70_Pr5-', 'SPO_BTA_')
    'SPO_BTA_MGO_'
    >>> add_to_team('MGO_PD_G0-_A14_DC43_H70_Pr5-', 'SPO_BTA_MGO_')
    'SPO_BTA_MGO_'
    >>> add_to_team('', 'HDU_GMC_CSN_MBA_')
    'HDU_GMC_CSN_MBA_'
    >>> add_to_team('', '')
    ''
    """
    if len(player) == 0:
        return roster

    player_id = get_player_id(player)

    if player_id in roster:
        return roster

    return roster + player_id + '_'


def remove_player(roster: str, roster_spot: int) -> str:
    """Return an updated copy of roster with the underscore at index
    roster_spot removed along with it's corresponding player ID. The
    corresponding player ID is the player ID located in front of the
    underscore at index roster_spot.

    Precondition: player is the string of player stats as
    seen in players.txt or the empty string. roster_spot is valid and
    non-negative. roster at index roster_spot must be occupied by an
    underscore "_".

    >>> remove_player('SPO_BTA_', 3)
    'BTA_'
    >>> remove_player('SPO_BTA_MGO_', -1)
    'SPO_BTA_MGO_'
    >>> remove_player('HDU_GMC_CSN_MBA_', 7)
    'HDU_CSN_MBA_'
    >>> remove_player('HDU_GMC_CSN_MBA_', 9)
    'HDU_GMC_CSN_MBA_'
    """
    if roster[roster_spot] != '_' or roster_spot < 0:
        return roster

    playerid_string = roster[(roster_spot - 3):(roster_spot + 1)]

    return roster.replace(playerid_string, "")


def compute_dc_points(player: str) -> int:
    """Return the number of points player accumulated via defensive
    contributions. Return 0 if player is a goalie or the empty string.

    Precondition: player is the string of player stats as
    seen in players.txt or the empty string

    >>> compute_dc_points('MGO_PD_G0-_A14_DC43_H70_Pr5-')
    8
    >>> compute_dc_points('NSH_PF_G7-_A14_DC20_H73_Pr10')
    2
    >>> compute_dc_points('CLA_PG_GAA2.23_SV0.910_Pr20')
    0
    >>> compute_dc_points('')
    0
    """
    player_position = get_position(player)

    if player_position == 'G' or player == '':
        return 0

    player_dc = int(player[17:19])

    if player_position == 'F':
        return player_dc // F_DCS_PER_POINT

    if player_position == 'D':
        return player_dc // D_DCS_PER_POINT

    return 0


def compute_goal_points(player: str) -> int:
    """Return the number of points player accumulated via scoring goals.
    Return 0 if player is a goalie or the empty string.

    Precondition: player is the string of player stats as
    seen in players.txt or the empty string

    >>> compute_goal_points('RRO_PF_G35_A35_DC43_H39_Pr25')
    140
    >>> compute_goal_points('NSH_PF_G7-_A14_DC20_H73_Pr10')
    28
    >>> compute_goal_points('CLA_PG_GAA2.23_SV0.910_Pr20')
    0
    >>> compute_goal_points('')
    0
    """

    player_position = get_position(player)

    if player_position == 'G' or player == '':
        return 0

    player_goals = player[8:10]

    return int(player_goals.rstrip("-")) * POINTS_PER_GOAL


def compute_assist_points(player: str) -> int:
    """Return the number of points player accumulated via assisting goals.
    Return 0 if player is a goalie or the empty string.

    Precondition: player is the string of player stats as
    seen in players.txt or the empty string

    >>> compute_assist_points('RRO_PF_G35_A35_DC43_H39_Pr25')
    70
    >>> compute_assist_points('NSH_PF_G7-_A14_DC20_H73_Pr10')
    28
    >>> compute_assist_points('CLA_PG_GAA2.23_SV0.910_Pr20')
    0
    >>> compute_assist_points('')
    0
    """

    player_position = get_position(player)

    if player_position == 'G' or player == '':
        return 0

    player_assists = player[12:14]

    return int(player_assists.rstrip("-")) * POINTS_PER_ASSIST


def compute_hit_points(player: str) -> int:
    """Return the number of points player accumulated via hits.
    Return 0.0 if player is a goalie or the empty string.

    Precondition: player is the string of player stats as
    seen in players.txt or the empty string

    >>> compute_hit_points('RRO_PF_G35_A35_DC43_H39_Pr25')
    9.75
    >>> compute_hit_points('NSH_PF_G7-_A14_DC20_H73_Pr10')
    18.25
    >>> compute_hit_points('CLA_PG_GAA2.23_SV0.910_Pr20')
    0.0
    >>> compute_hit_points('')
    0.0
    """

    player_position = get_position(player)

    if player_position == 'G' or player == '':
        return 0.0

    player_hits = player[21:23]

    return float(player_hits.rstrip("-")) * POINTS_PER_HIT


def compute_fantasy_score(player: str) -> float:
    """Return the total fantsay points accumulated by player. For skaters,
    this consists of goal points, hit points, dc points and assist points.
    For goalies, this is calculated depending on save percentage and goals
    against average found on the player string of data. If player is the
    empty string, returns 0.0.

    Precondition: player is the string of player stats as
    seen in players.txt or the empty string

    >>> compute_fantasy_score('RRO_PF_G35_A35_DC43_H39_Pr25')
    223.75
    >>> compute_fantasy_score('NSH_PF_G7-_A14_DC20_H73_Pr10')
    76.25
    >>> compute_fantasy_score('GMC_PG_GAA2.57_SV0.902_Pr15')
    64.5
    >>> compute_fantasy_score('')
    0.0
    """

    if len(player) == 0:
        return 0.0

    player_position = get_position(player)

    hp = compute_hit_points(player)
    ap = compute_assist_points(player)
    dcp = compute_dc_points(player)
    gp = compute_goal_points(player)

    if player_position in {'F', 'D'}:
        return hp + ap + dcp + gp

    gaa = float(player[10:14])
    sv = float(player[17:22])

    if player_position == 'G':
        return (SV_VALUE * sv) - (GAA_VALUE * gaa)

    return 0.0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
