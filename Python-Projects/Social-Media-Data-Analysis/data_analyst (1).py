"""CSCA08: Fall 2025 -- Assignment 3: Social Media Data Analyst

Starter code.

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2025 Jacqueline Smith, David Liu, Dominik Luszczynski,
and anya Tafliovich

"""

from typing import TextIO
from copy import deepcopy

from constants import (
    UserData,
    AccountData,
    DOB,
    NUM_POSTS,
    NUM_COMMENTS,
    ACCOUNT_CREATED,
    FOLLOWERS,
    FOLLOWING,
    NUM_MUTUALS,
    BOT_GROUPS,
    SEP,
    USERNAME_COL,
    DOB_COL,
    NUM_POSTS_COL,
    NUM_COMMENTS_COL,
    ACCOUNT_CREATED_COL,
    FOLLOWER_COL,
    FOLLOWING_COL,
    HCLP,
    HCLM,
    HCNA,
    HFLF,
    P_HCLM_COMMENT,
    P_HCLM_MUTUALS,
    P_HCLP_COMMENT,
    P_HCLP_POSTS,
    P_HCNA_COMMENT,
    HFLF_FACTOR,
)

SAMPLE_DATA = {
    "username1": {
        DOB: "1973-01-06",
        NUM_POSTS: 3,
        NUM_COMMENTS: 8,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username2"],
        FOLLOWING: ["username2", "username4"],
        BOT_GROUPS: [],
    },
    "username2": {
        DOB: "1973-01-06",
        NUM_POSTS: 5,
        NUM_COMMENTS: 5,
        ACCOUNT_CREATED: "2025-01-01",
        FOLLOWERS: ["username1", "username3"],
        FOLLOWING: [
            "username1",
            "username3",
        ],
        BOT_GROUPS: [],
    },
    "username3": {
        DOB: "1973-01-06",
        NUM_POSTS: 0,
        NUM_COMMENTS: 11,
        ACCOUNT_CREATED: "2025-01-01",
        FOLLOWERS: ['username2'],
        FOLLOWING: ["username2", "username4", "username5"],
        BOT_GROUPS: [],
    },
    "username4": {
        DOB: "1973-01-06",
        NUM_POSTS: 10,
        NUM_COMMENTS: 1,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username1",
                    "username3",
                    "username5"],
        FOLLOWING: [],
        BOT_GROUPS: [],
    },
    "username5": {
        DOB: "1973-01-06",
        NUM_POSTS: 2,
        NUM_COMMENTS: 10,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username3"],
        FOLLOWING: ["username4"],
        BOT_GROUPS: [],
    },
}

SAMPLE_DATA_WITH_NUM_MUTUALS = {
    "username1": {
        DOB: "1973-01-06",
        NUM_POSTS: 3,
        NUM_COMMENTS: 8,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username2"],
        FOLLOWING: ["username2", "username4"],
        BOT_GROUPS: [],
        NUM_MUTUALS: 1
    },
    "username2": {
        DOB: "1973-01-06",
        NUM_POSTS: 5,
        NUM_COMMENTS: 5,
        ACCOUNT_CREATED: "2025-01-01",
        FOLLOWERS: ["username1", "username3"],
        FOLLOWING: [
            "username1",
            "username3",
        ],
        BOT_GROUPS: [],
        NUM_MUTUALS: 2,
    },
    "username3": {
        DOB: "1973-01-06",
        NUM_POSTS: 0,
        NUM_COMMENTS: 11,
        ACCOUNT_CREATED: "2025-01-01",
        FOLLOWERS: ['username2'],
        FOLLOWING: ["username2", "username4", "username5"],
        BOT_GROUPS: [],
        NUM_MUTUALS: 1
    },
    "username4": {
        DOB: "1973-01-06",
        NUM_POSTS: 10,
        NUM_COMMENTS: 1,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username1", "username3", "username5"],
        FOLLOWING: [],
        BOT_GROUPS: [],
        NUM_MUTUALS: 0
    },
    "username5": {
        DOB: "1973-01-06",
        NUM_POSTS: 2,
        NUM_COMMENTS: 10,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username3"],
        FOLLOWING: ["username4"],
        BOT_GROUPS: [],
        NUM_MUTUALS: 0
    },
}

SAMPLE_DATA_FULL = {
    "username1": {
        DOB: "1973-01-06",
        NUM_POSTS: 3,
        NUM_COMMENTS: 8,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username2"],
        FOLLOWING: ["username2", "username4"],
        BOT_GROUPS: [],
        NUM_MUTUALS: 1
    },
    "username2": {
        DOB: "1973-01-06",
        NUM_POSTS: 5,
        NUM_COMMENTS: 5,
        ACCOUNT_CREATED: "2025-01-01",
        FOLLOWERS: ["username1", "username3"],
        FOLLOWING: [
            "username1",
            "username3",
        ],
        BOT_GROUPS: [],
        NUM_MUTUALS: 2,
    },
    "username3": {
        DOB: "1973-01-06",
        NUM_POSTS: 0,
        NUM_COMMENTS: 11,
        ACCOUNT_CREATED: "2025-01-01",
        FOLLOWERS: ['username2'],
        FOLLOWING: ["username2", "username4", "username5"],
        BOT_GROUPS: ['highCommentsNewAccount',
                     'highFollowingLowFollowers',
                     'highCommentsLowPosts'],
        NUM_MUTUALS: 1
    },
    "username4": {
        DOB: "1973-01-06",
        NUM_POSTS: 10,
        NUM_COMMENTS: 1,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username1", "username3", "username5"],
        FOLLOWING: [],
        BOT_GROUPS: [],
        NUM_MUTUALS: 0
    },
    "username5": {
        DOB: "1973-01-06",
        NUM_POSTS: 2,
        NUM_COMMENTS: 10,
        ACCOUNT_CREATED: "2023-01-01",
        FOLLOWERS: ["username3"],
        FOLLOWING: ["username4"],
        BOT_GROUPS: ['highCommentsLowMutuals'],
        NUM_MUTUALS: 0
    },
}


# TASK ONE

# We provide the header and docstring for this function to get you
# started and to demonstrate that there are no docstring examples in
# functions that read from files.
def create_users_dictionary(users_file: TextIO) -> UserData:
    """Return a dictionary (no duplicates) created from
    the file users_file in the form of the UserData:

    {
        username: {
            DOB : dob,
            NUM_POSTS: num_posts,
            NUM_COMMENTS: num_comments,
            ACCOUNT_CREATED: account_created,
            FOLLOWERS: [],
            FOLLOWING: [],
            BOT_GROUPS: []
        }
        ...
    }

    Precondition: users_file is open for reading
                  users_file is in the format described in the handout

    """
    users_dict: UserData = {}

    users_file.readline()

    for line in users_file:
        line = line.strip()
        if not line:
            continue  # skip blank lines if any

        (username, dob, num_posts_str,
         num_comments_str, account_created) = line.split(',')

        num_posts = int(num_posts_str)
        num_comments = int(num_comments_str)

        users_dict[username] = {
            DOB: dob,
            NUM_POSTS: num_posts,
            NUM_COMMENTS: num_comments,
            ACCOUNT_CREATED: account_created,
            FOLLOWERS: [],
            FOLLOWING: [],
            BOT_GROUPS: [],
            NUM_MUTUALS: 0
        }

    return users_dict


def add_followers(users_dict: UserData, followers_file: TextIO) -> None:
    """Modifies users_dict to update the users FOLLOWERS and FOLLOWING
    list statuses from follower_file.

    Preconditions:
    - Both users must already appear in users_dict.
    - Each user is not a duplicate
    - followers_file is open for reading and correctly formatted.
    """
    followers_file.readline()

    for line in followers_file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(SEP)
        follower = parts[FOLLOWER_COL].strip()
        following = parts[FOLLOWING_COL].strip()

        if follower not in users_dict or following not in users_dict:
            continue

        if follower not in users_dict[following][FOLLOWERS]:
            users_dict[following][FOLLOWERS].append(follower)

        if following not in users_dict[follower][FOLLOWING]:
            users_dict[follower][FOLLOWING].append(following)

# TASK TWO

# We provide the header and part of a docstring for this function to
# get you started and to demonstrate the use of function deepcopy in
# examples that modify input data.


def add_num_mutual_connections(users_dict: UserData) -> None:
    """Modify the dictionary users_dict by adding the number of
    mutual relationships each user has using the NUM_MUTUALS key.

    Note a mutual relationship occurs when two users follow each
    other.


    >>> sample_data_copy = deepcopy(SAMPLE_DATA)
    >>> add_num_mutual_connections(sample_data_copy)
    >>> sample_data_copy['username1'][NUM_MUTUALS] == 1
    True
    >>> sample_data_copy['username2'][NUM_MUTUALS] == 2
    True
    """

    for username in users_dict:

        followers_set = set(users_dict[username][FOLLOWERS])
        following_set = set(users_dict[username][FOLLOWING])

        mutuals = followers_set.intersection(following_set)

        users_dict[username][NUM_MUTUALS] = len(mutuals)


def get_quantile(values: list[int], p: float) -> int:
    """Return the quantile in which p can be found relative to the number of
    items in values. If p is not in the iterval [0,1],
    or values is empty, return -1.
    """

    if not values or p < 0.0 or p > 1.0:
        return -1

    sorted_values = sorted(values)
    n = len(sorted_values)

    index = int(p * (n - 1))

    return sorted_values[index]


def add_bot_candidate_groups(users_dict: UserData) -> None:
    """Modifies users_dict by adding each of the four possible bot
    candidate groups to each user if and only if they meet the criteria
    for said BOT_GROUP.

    Preconditions: add_followers and add_num_mutual_connections
    functions have been called.

    """
    num_comments_list = []
    num_posts_list = []
    num_mutuals_list = []

    for username in users_dict:
        account = users_dict[username]
        num_comments_list.append(account[NUM_COMMENTS])
        num_posts_list.append(account[NUM_POSTS])
        num_mutuals_list.append(account[NUM_MUTUALS])

    thresholds = ({
        'hclp_comment': get_quantile(num_comments_list, P_HCLP_COMMENT),
        'hclp_posts': get_quantile(num_posts_list, P_HCLP_POSTS),
        'hclm_comment': get_quantile(num_comments_list, P_HCLM_COMMENT),
        'hclm_mutuals': get_quantile(num_mutuals_list, P_HCLM_MUTUALS),
        'hcna_comment': get_quantile(num_comments_list, P_HCNA_COMMENT),
        'hcna_cutoff': '2023-01-01'})

    for username, acc in users_dict.items():

        groups = acc[BOT_GROUPS]

        if (acc[NUM_COMMENTS] >= thresholds['hclp_comment']
                and acc[NUM_POSTS] <= thresholds['hclp_posts']
                and HCLP not in groups):
            groups.append(HCLP)

        if (acc[NUM_COMMENTS] >= thresholds['hclm_comment']
                and acc[NUM_MUTUALS] <= thresholds['hclm_mutuals']
                and HCLM not in groups):
            groups.append(HCLM)

        if (acc[NUM_COMMENTS] >= thresholds['hcna_comment']
                and acc[ACCOUNT_CREATED] > thresholds['hcna_cutoff']
                and HCNA not in groups):
            groups.append(HCNA)

        if (len(acc[FOLLOWERS]) > 0
                and len(acc[FOLLOWING]) > HFLF_FACTOR * len(acc[FOLLOWERS])
                and HFLF not in groups):
            groups.append(HFLF)

# TASK THREE


def find_all_bot_candidates(users_dict: UserData) -> UserData:
    """Return a new users_dict dictionary of all users who fit the
    criteria to  be a bot.

    Preconditions: add_bot_candidate_groups has been called before
    using this function.

    >>> users_dict = {
    ...   'krogers': {BOT_GROUPS: ['HCLP'], FOLLOWERS: [], FOLLOWING: []},
    ...    'emeyer': {BOT_GROUPS: [], FOLLOWERS: [], FOLLOWING: []}
    ...    }
    >>> result = find_all_bot_candidates(users_dict)
    >>> sorted(list(result.keys()))
    ['krogers']
    """

    bot_candidates: users_dict = {}

    for username, data in users_dict.items():
        if len(data[BOT_GROUPS]) > 0:
            bot_candidates[username] = data.copy()

    return bot_candidates


def find_users_abusing_system(users_dict: UserData) -> UserData:
    """Return a new users_dict dictionary of all users who are using bots to
    abuse the monetisation system. A person is abusing the monetisation system
    if and only if bot candidates accumulate to more than 50% of their
    FOLLOWERS list.

    Precondition: add_bot_candidate_groups function has been called.

    # From users_small.csv

    >>> users_dict = {
    ...    'krogers': {BOT_GROUPS: ['HCLP'], FOLLOWERS: []},
    ...    'emeyer': {BOT_GROUPS: ['HCLM'], FOLLOWERS: []},
    ...    'allison45': {BOT_GROUPS: [], FOLLOWERS: ['krogers', 'emeyer']}}
    >>> abusing_users = find_users_abusing_system(users_dict)
    >>> list(abusing_users.keys())
    ['allison45']
    """

    abusing_users: UserData = {}

    bot_usernames = set()
    for name, account in users_dict.items():
        if account[BOT_GROUPS]:
            bot_usernames.add(name)
        followers = account[FOLLOWERS]

        bot_count = 0
        for follower_username in followers:
            if follower_username in bot_usernames:
                bot_count += 1

            if bot_count > len(followers) / 2:
                abusing_users[name] = account.copy()

    return abusing_users

# TASK FOUR


def order_bot_candidates(users_dict: UserData) -> list[str]:
    """Return a list of bot candidate usernames from users_dict, sorted by
    the number of BOT_GROUPS the user belongs to in decreasing order. If two
    users belong to the same numbe rof groups, then sort alphabetically by
    username in a decreasing fashion. (Z to A)

    Precondition: the list should only contain bot candidates. Also, the
    dictionary passed will have all keys in AccountData.

    >>> users = {
    ...    'krogers': {BOT_GROUPS: ['HCLP', 'HCNA']},
    ...    'bellpeter': {BOT_GROUPS: ['HCLM', 'HFLF']},
    ...    'emeyer': {BOT_GROUPS: ['HCLM']},
    ...    'wcosta': {BOT_GROUPS: []}}
    >>> order_bot_candidates(users)
    ['krogers', 'bellpeter', 'emeyer']
    """

    bot_usernames = []

    for username, data in users_dict.items():
        if len(data[BOT_GROUPS]) > 0:
            bot_usernames.append(username)

    bot_usernames.sort(reverse=True)

    keyed_list = []
    for username in bot_usernames:
        num_groups = len(users_dict[username][BOT_GROUPS])
        keyed_list.append((num_groups, username))

    keyed_list.sort(reverse=True)

    ordered_usernames = []
    for num_groups, username in keyed_list:
        ordered_usernames.append(username)

    return ordered_usernames


def order_users_abusing_system(users_dict: UserData) -> list[str]:
    """Return a list of usernames from users_dict, sorted by the number of
    followers who are bot candidates in decreasing order. If two users have the
    same number of bot followers, then sort alphabetically by username in a
    decreasing fashion. (Z to A)

    Precondition: the list should only contain users wggo abuse the system.
    Also, the dictionary passed will have all keys in AccountData.

    >>> users = {'krogers': {BOT_GROUPS: ['HCLP'], FOLLOWERS: []},
    ...    'emeyer': {BOT_GROUPS: ['HCLM'], FOLLOWERS: []},
    ...    'allison45': {BOT_GROUPS: [], FOLLOWERS: ['krogers']},
    ...    'wcosta': {BOT_GROUPS: [], FOLLOWERS: ['emeyer']}}
    >>> order_users_abusing_system(users)
    ['wcosta', 'allison45']
    """

    bot_candidates = []
    abusing_list = []

    for username, data in users_dict.items():
        if len(data[BOT_GROUPS]) > 0:
            bot_candidates.append(username)

    for username1, data in users_dict.items():
        followers = data[FOLLOWERS]

        bot_count = 0

        for f in followers:
            if f in bot_candidates:
                bot_count += 1

        if bot_count > len(followers) / 2:
            abusing_list.append(username1)

    abusing_list.sort(reverse=True)

    return abusing_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    '''
    Uncomment the code below when you are ready to test.

    The code below uses the small dataset. If you wish to use the
    larger dataset, please replace _small with _medium.
    '''

    # with open("users_small.csv", "r") as f:
    #     all_users = create_users_dictionary(f)

    # with open("followers_small.csv", "r") as f:
    #     add_followers(all_users, f)

    # add_num_mutual_connections(all_users)

    # add_bot_candidate_groups(all_users)

    # all_bot_candidates = find_all_bot_candidates(all_users)
    # users_using_bots = find_users_abusing_system(all_users)
    # bot_candidate_order = order_bot_candidates(all_users)
    # users_using_bots_order = order_users_abusing_system(all_users)

    # print("=" * 50)
    # print('Bot Candidates: ')
    # print("=" * 50)
    # print(bot_candidate_order)
    # print("=" * 50)
    # print('Users Using Bots: ')
    # print("=" * 50)
    # print(users_using_bots_order)
