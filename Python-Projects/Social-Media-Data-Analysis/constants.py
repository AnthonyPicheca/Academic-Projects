# UserData type: keys are usernames, values are account data
# AccountData type: keys are strings and values can be either
#                   str, list[str] or an int
AccountData = dict[str, str | list[str] | int]
UserData = dict[str, AccountData]

# Dictionary Keys
USERNAME = 'username'
DOB = 'dob'
NUM_POSTS = 'num_posts'
NUM_COMMENTS = 'num_comments'
ACCOUNT_CREATED = 'account_created'
FOLLOWERS = 'followers'
FOLLOWING = 'following'
NUM_MUTUALS = 'num_mutuals'
BOT_GROUPS = 'bot_groups'

# Column indexes for users file
USERNAME_COL = 0 # username
DOB_COL = 1 # date of birth
NUM_POSTS_COL = 2 # number of posts made
NUM_COMMENTS_COL = 3 # number of comments made
ACCOUNT_CREATED_COL = 4 # date of account creation

# Column indexes for follower file
FOLLOWER_COL = 0
FOLLOWING_COL = 1

# seperator for reading files
SEP = ','

# Bot Group Names
HCLP = 'highCommentsLowPosts'
HCLM = 'highCommentsLowMutuals'
HCNA = 'highCommentsNewAccount'
HFLF = 'highFollowingLowFollowers'

# Bot Group quantiles and Factors
P_HCLP_COMMENT = 0.9
P_HCLP_POSTS = 0.1
P_HCLM_COMMENT = 0.8
P_HCLM_MUTUALS = 0.1
P_HCNA_COMMENT = 0.75
HFLF_FACTOR = 2
