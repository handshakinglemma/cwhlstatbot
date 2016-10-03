# most_stat
# Selects a random stat and returns the player with the most stat.
# Formats and returns a tweet.

import random

# most_stat
# Finds the player with the most stat
# INPUT: stats, player_dicts
# The list of stats and the list of players' stat dictionaries.
# OUTPUT: most_stat, most_player, tied_players, category
# The most calculated stat, the name of the player with the most stat, 
# a list that may contain the name of a player tied for most stat, and
# the categories used to calculate the most stat.
# (list, list) -> (float, str, list, str)
def most_stat(stats, player_dicts):

    # Get a random stat.
    category = stats[random.randint(0, len(stats) - 1)]

    # Initalize empty variables to catch most values.
    most = 0
    most_player = None
    most_team = None
    tied_players = []

    # Loop through all players.
    for d in player_dicts:
        
        # Get the player's stat.
        stat = d[category]
        
        # If the player's stat is better than the last, replace it.
        if stat > most:
            most = stat
            most_player = d['PLAYER']
            most_team = d['TEAM']
            tied_players = []

        # If players are tied, keep track of them.
        elif stat == most:
            tied_players.append(d['PLAYER'])
            tied_players.append(d['TEAM'])

        # If there is more than one tied player or if no player was
        # found, then recalculate.
        if len(tied_players) != 0 or most_player == None:
            most, most_player, most_team, tied_players, category = most_stat(stats, player_dicts)

    return most, most_player, most_team, tied_players, category

# tweet
# Formats and returns the tweet.
# INPUT: stats, player_dicts, abbreviations
# The list of stats, the list of players' stat dictionaries, and the
# dictonary of abbreviations for the various stats.
# OUTPUT: The string of the tweet.
def tweet(stats, player_dicts, abbreviations, prefix):

    # Get the data for the tweet.
    stat, player, team, tied, category = most_stat(stats, player_dicts)
    
    # Make the tweet.
    if len(tied) == 0:
        tweet = prefix[category] + ' ' + abbreviations[category] + ':' + '\n' + player + ' (' + team + ') with ' + str(stat)
    elif len(tied) == 2:
        tweet = prefix[category] + ' ' + abbreviations[category] + ':' + '\n' + player + ' (' + team + ') and ' + tied[0] + ' (' + tied[1] + ') with ' + str(stat)

    return tweet
