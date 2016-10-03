# most_stat_per
# Selects two random stats and returns the player with the best stat
# per the other stat. It recalculates if more than two players are tied
# for best stat.

import random

# most_stat_per
# INPUT: stats, player_dicts
# The list of stats and the list of players' stat dictionaries.
# OUTPUT: best_stat, best_player, tied_players, category1, category2
# The best calculated stat per stat, the name of the player
# with the best stat, a list that may contain the name of a player
# tied for best stat, and the two categories used to calculate the best
# stat per stat.
# (list, list) -> (float, str, list, str, str)
def most_stat_per(stats, player_dicts):

    # Generate two random stats categories.
    category1 = stats[random.randint(0, len(stats) - 1)]
    category2 = stats[random.randint(0, len(stats) - 1)]
    if category1 == category2:
        category1 = stats[random.randint(0, len(stats) - 1)]
        category2 = stats[random.randint(0, len(stats) - 1)]
        
    # Initialize empty variables to catch best values.
    best_stat = 0
    best_player = None
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
            if stat > best_stat:
                best_stat = stat
                best_player = d['PLAYER']
                tied_players = []

            # If players are tied, keep track of them.
            elif stat == best_stat:
                tied_players.append(d['PLAYER'])

    # If there are more than two players tied or if there was no
    # player calculated, recalculate.
    if len(tied_players) > 1 or best_player == None:
        # TODO: write intersting output to a file
        best_stat, best_player, tied_players, category1, category2 = best_stats_per(stats, player_dicts)
        
    return best_stat, best_player, tied_players, category1, category2

# tweet
# Formats and returns the tweet.
# INPUT: stats, player_stats, abbreviations
# The list of stats, the list of players' stat dictionaries, and the
# dictonary of abbreviations for the various stats.
# OUTPUT: The string of the tweet.
def tweet(stats, player_stats, abbreviations):

    # Get the data for the tweet.
    stat, player, tied, stat1, stat2 = most_stat_per(stats, player_stats)
    
    # Make the tweet.
    tweet = 'Most ' + abbreviations[stat1] + ' per ' + abbreviations[stat2] + ':' + '\n' + player + " with " + str(stat) + ' ' + stat1 + ' per ' + stat2 + '.'
    
    return tweet
