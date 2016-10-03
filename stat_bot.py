from read_file import read_file
import most_stat_per
import most_stat
import team_most_per
import random
from secret import *
import tweepy


def main():

    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
    api = tweepy.API(auth) 

    skaters = read_file('skaters.csv')
    goalies = read_file('goalies.csv')

    skater_stats = ['games played', 'goals', 'assists', 'points', 'plus-minus', 'penalty minutes', 'power play goals', 'power play assists', 'short-handed goals', 'short-handed assists', 'game winning goals']
    goalie_stats = ['games played', 'minutes played', 'wins', 'losses', 'overtime losses', 'shootout losses', 'shutouts', 'goals against', 'goals against average', 'saves', 'save percentage']

    goalie_stat_list = ['#', 'GP', 'W', 'L', 'OTL', 'SOL', 'SO', 'GA', 'GAA', 'SV', 'SV%']

    skater_stat_list = ['#', 'GP', 'G', 'A', 'PTS', '+/-', 'PIM', 'PP', 'PPA', 'SH', 'SHA', 'GWG']

    abbreviations = {'#':'jersey number', 'GP':'games played', 'MIN':'minutes played', 'W':'wins', 'L':'losses', 'OTL':'overtime losses', 'SOL':'shootout losses', 'SO':'shutouts', 'GA':'goals against', 'GAA':'goals against average', 'SV':'saves', 'SV%':'save percentage', 'G':'goals', 'A':'assists', 'PTS':'points', '+/-':'plus-minus', 'PIM':'penalty minutes', 'PP':'power play goals', 'PPA':'power play assists', 'SH':'short-handed goals', 'SHA':'short-handed assists', 'GWG':'game winning goals'}

    prefix = {'#':'Highest', 'GP':'Most', 'MIN':'Most', 'W':'Most', 'L':'Most', 'OTL':'Most', 'SOL':'Most', 'SO':'Most', 'GA':'Most', 'GAA':'Highest', 'SV':'Most', 'SV%':'Highest', 'G':'Most', 'A':'Most', 'PTS':'Most', '+/-':'Highest', 'PIM':'Most', 'PP':'Most', 'PPA':'Most', 'SH':'Most', 'SHA':'Most', 'GWG':'Most'}


    # Generate a random number to decide what kind of stat to tweet.
    epsilon = random.random()
    # Total number of possible stats to tweet.
    total = 6

    # Make the tweet!
    if epsilon < (1 / total):
        tweet = most_stat_per.tweet(skater_stat_list, skaters, abbreviations)
    elif epsilon < (2 / total):
        tweet = most_stat_per.tweet(goalie_stat_list, goalies, abbreviations)
    elif epsilon < (3 / total):
        tweet = most_stat.tweet(skater_stat_list, skaters, abbreviations, prefix)
    elif epsilon < (4 / total):
        tweet = most_stat.tweet(goalie_stat_list, goalies, abbreviations, prefix)
    elif epsilon < (5 / total):
        tweet = team_most_per.tweet(skater_stat_list, skaters, abbreviations)
    else:
        tweet = team_most_per.tweet(goalie_stat_list, goalies, abbreviations)

    # Tweet the tweet!
    api.update_status(tweet)
        
main()
