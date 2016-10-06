# team_most_per
# Selects two random stats and returns the team with the most stat
# per the other stat. It recalculates if more than two teams are tied
# for most stat. Formats and returns a tweet.

import random
from decimal import *

# team_most_per
# Caluclates the most stat per stat.
# INPUT: stats, player_dicts
# The list of stats and the list of players' stat dictionaries.
# OUTPUT: most_stat, most_player, tied_players, category1, category2
# The most calculated stat per stat, the name of the player
# with the most stat, a list that may contain the name of a player
# tied for most stat, and the two categories used to calculate the most
# stat per stat.
# (list, list) -> (float, str, list, str, str)
def team_most_per(stats, player_dicts):

    # Generate two random stats categories.
    category1 = stats[random.randint(0, len(stats) - 1)]
    category2 = stats[random.randint(0, len(stats) - 1)]

    # Re-generate if the chosen categories are the same.
    if category1 == category2:
        category1 = stats[random.randint(0, len(stats) - 1)]
        category2 = stats[random.randint(0, len(stats) - 1)]

    # Initalize empty lists to catch stats for all teams.
    stat1 = [0, 0, 0, 0, 0]
    stat2 = [0, 0, 0, 0, 0]
    # statX[0] -> BOS
    # statX[1] -> BRA
    # statX[2] -> CAL
    # statX[3] -> MON
    # statX[4] -> TOR

    for d in player_dicts:

        if d['TEAM'] == 'BOS':
            stat1[0] += d[category1]
            stat2[0] += d[category2]
        elif d['TEAM'] == 'BRA':
            stat1[1] += d[category1]
            stat2[1] += d[category2]
        elif d['TEAM'] == 'CAL':
            stat1[2] += d[category1]
            stat2[2] += d[category2]
        elif d['TEAM'] == 'MON':
            stat1[3] += d[category1]
            stat2[3] += d[category2]
        elif d['TEAM'] == 'TOR':
            stat1[4] += d[category1]
            stat2[4] += d[category2]

    # Initialize empty variables to catch most values.
    most_stat = 0
    most_team = None
    tied_teams = []

    # Loop through all team stats.
    for i in range(len(stat1)):

        # Avoid division by 0.
        if stat2[i] > 0:

            # Calculate new stat!
            stat = stat1[i] / stat2[i]

            if stat > most_stat:
                most_stat = stat
                most_team = i
                tied_teams = []

            elif stat == most_stat:
                tied_teams.append(i)

    # If there are more than two teams tied or if there was no
    # team calculated, recalculate.
    if len(tied_teams) > 1 or most_team == None:
        # TODO: write intersting output to a file
        most_stat, most_team, tied_teams, category1, category2 = team_most_per(stats, player_dicts)
        
    return most_stat, most_team, tied_teams, category1, category2

# tweet
# Formats and returns the tweet.
# INPUT: stats, player_dicts, abbreviations
# The list of stats, the list of players' stat dictionaries, and the
# dictonary of abbreviations for the various stats.
# OUTPUT: The string of the tweet.
def tweet(stats, player_dicts, abbreviations):

    # Get the data for the tweet.
    stat, team, tied, stat1, stat2 = team_most_per(stats, player_dicts)

    # Team abbreviations key.
    teams = ['Boston Blades', 'Brampton Thunder', 'Calgary Inferno', 'Canadiennes de Montreal', 'Toronto Furies']
    
    # Make the tweet.

    # No tied teams.
    if len(tied) == 0:
        
        # If the stat has more than 5 decimal places, truncate it.
        if abs(Decimal(str(stat)).as_tuple().exponent) > 5:
            tweet = ('2015-16 Most ' + abbreviations[stat1] + ' per ' + abbreviations[stat2] + ':' + '\n' + 'The ' + teams[team] + ' with ' + '{:.3f}' + ' ' + stat1 + ' per ' + stat2).format(stat)

        else:
            tweet = '2015-16 Most ' + abbreviations[stat1] + ' per ' + abbreviations[stat2] + ':' + '\n' + 'The ' + teams[team] + ' with ' + str(stat) + ' ' + stat1 + ' per ' + stat2

    # Two tied teams.
    elif len(tied) == 2:

        # If the stat has more than 5 decimal places, truncate it.
        if abs(Decimal(str(stat)).as_tuple().exponent) > 5:
            tweet = ('2015-16 Most ' + abbreviations[stat1] + ' per ' + abbreviations[stat2] + ':' + '\n' + 'The ' + teams[team] + ' and the ' + teams[tied[0]] + ' with ' + '{:.3f}' + ' ' + stat1 + ' per ' + stat2).format(stat)
            
        else:
            tweet = '2015-16 Most ' + abbreviations[stat1] + ' per ' + abbreviations[stat2] + ':' + '\n' + 'The ' + teams[team] + ' and the ' + teams[tied[0]] + ' with ' + str(stat) + ' ' + stat1 + ' per ' + stat2
    
    return tweet
