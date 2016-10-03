# most_stat_per
# Selects two random stats and returns the player with the most stat
# per the other stat. It recalculates if more than two players are tied
# for most stat. Formats and returns a tweet.

import random
from decimal import *

# most_stat_per
# Caluclates the most stat per stat.
# INPUT: stats, player_dicts
# The list of stats and the list of players' stat dictionaries.
# OUTPUT: most_stat, most_player, tied_players, category1, category2
# The most calculated stat per stat, the name of the player
# with the most stat, a list that may contain the name of a player
# tied for most stat, and the two categories used to calculate the most
# stat per stat.
# (list, list) -> (float, str, list, str, str)
def most_stat_per(stats, player_dicts):

    # Generate two random stats categories.
    category1 = stats[random.randint(0, len(stats) - 1)]
    category2 = stats[random.randint(0, len(stats) - 1)]
    if category1 == category2:
        category1 = stats[random.randint(0, len(stats) - 1)]
        category2 = stats[random.randint(0, len(stats) - 1)]
        
    # Initialize empty variables to catch most values.
    most_stat = 0
    most_player = None
    most_team = None
    tied_players = []

    # Loop through all players.
    for d in player_dicts:

        # Get the player's stats for the two categories.
        stat1 = d[category1]
        stat2 = d[category2]

        # Avoid division by 0.
        if stat2 > 0:
            
            # Calculate new stat!
            stat = stat1 / stat2
            
            # If this player's stat is better than the last, replace it.
            if stat > most_stat:
                most_stat = stat
                most_player = d['PLAYER']
                most_team = d['TEAM']
                tied_players = []

            # If players are tied, keep track of them.
            elif stat == most_stat:
                tied_players.append(d['PLAYER'])
                tied_players.append(d['TEAM'])

    # If there are more than two players tied or if there was no
    # player calculated, recalculate.
    if len(tied_players) > 2 or most_player == None:
        # TODO: write intersting output to a file
        most_stat, most_player, most_team, tied_players, category1, category2 = most_stat_per(stats, player_dicts)
        
    return most_stat, most_player, most_team, tied_players, category1, category2

# tweet
# Formats and returns the tweet.
# INPUT: stats, player_dicts, abbreviations
# The list of stats, the list of players' stat dictionaries, and the
# dictonary of abbreviations for the various stats.
# OUTPUT: The string of the tweet.
def tweet(stats, player_dicts, abbreviations):

    # Get the data for the tweet.
    stat, player, team, tied, stat1, stat2 = most_stat_per(stats, player_dicts)

    # Make the tweet.
    if len(tied) == 0:
        # If the stat has more than 5 decimal places, truncate it.
        if abs(Decimal(str(stat)).as_tuple().exponent) > 5:
            tweet = ('2015-16 Most ' + abbreviations[stat1] + ' per ' + abbreviations[stat2] + ':' + '\n' + player + ' (' + team + ') with ' + '{:.3f}' + ' ' + stat1 + ' per ' + stat2).format(stat)
        else:
            tweet = '2015-16 Most ' + abbreviations[stat1] + ' per ' + abbreviations[stat2] + ':' + '\n' + player + ' (' + team + ') with ' + str(stat) + ' ' + stat1 + ' per ' + stat2
    elif len(tied) == 2:
        if abs(Decimal(str(stat)).as_tuple().exponent) > 5:
            tweet = ('2015-16 Most ' + abbreviations[stat1] + ' per ' + abbreviations[stat2] + ':' + '\n' + player + ' (' + team + ') and ' + tied[0] + ' (' + tied[1] + ') with ' + '{:.3f}' + ' ' + stat1 + ' per ' + stat2).format(stat)
        else:
            tweet = '2015-16 Most ' + abbreviations[stat1] + ' per ' + abbreviations[stat2] + ':' + '\n' + player + ' (' + team + ') and ' + tied[0] + ' (' + tied[1] + ') with ' + str(stat) + ' ' + stat1 + ' per ' + stat2
    
    return tweet
