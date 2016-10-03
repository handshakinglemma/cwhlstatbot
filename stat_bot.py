from read_file import read_file
import most_stat_per
import most_stat
import team_most_per

def main():

    skaters = read_file('skaters.csv')
    goalies = read_file('goalies.csv')

    skater_stats = ['games played', 'goals', 'assists', 'points', 'plus-minus', 'penalty minutes', 'power play goals', 'power play assists', 'short-handed goals', 'short-handed assists', 'game winning goals']
    goalie_stats = ['games played', 'minutes played', 'wins', 'losses', 'overtime losses', 'shootout losses', 'shutouts', 'goals against', 'goals against average', 'saves', 'save percentage']

    goalie_stat_list = ['#', 'GP', 'W', 'L', 'OTL', 'SOL', 'SO', 'GA', 'GAA', 'SV', 'SV%']

    skater_stat_list = ['#', 'GP', 'G', 'A', 'PTS', '+/-', 'PIM', 'PP', 'PPA', 'SH', 'SHA', 'GWG']

    abbreviations = {'#':'jersey number', 'GP':'games played', 'MIN':'minutes played', 'W':'wins', 'L':'losses', 'OTL':'overtime losses', 'SOL':'shootout losses', 'SO':'shutouts', 'GA':'goals against', 'GAA':'goals against average', 'SV':'saves', 'SV%':'save percentage', 'G':'goals', 'A':'assists', 'PTS':'points', '+/-':'plus-minus', 'PIM':'penalty minutes', 'PP':'power play goals', 'PPA':'power play assists', 'SH':'short-handed goals', 'SHA':'short-handed assists', 'GWG':'game winning goals'}

    prefix = {'#':'Highest', 'GP':'Most', 'MIN':'Most', 'W':'Most', 'L':'Most', 'OTL':'Most', 'SOL':'Most', 'SO':'Most', 'GA':'Most', 'GAA':'Highest', 'SV':'Most', 'SV%':'Highest', 'G':'Most', 'A':'Most', 'PTS':'Most', '+/-':'Highest', 'PIM':'Most', 'PP':'Most', 'PPA':'Most', 'SH':'Most', 'SHA':'Most', 'GWG':'Most'}

    
    s1 = most_stat_per.tweet(skater_stat_list, skaters, abbreviations)
    print(s1)

    g1 = most_stat_per.tweet(goalie_stat_list, goalies, abbreviations)
    print(g1)

    s2 = most_stat.tweet(skater_stat_list, skaters, abbreviations, prefix)
    print(s2)

    g2 = most_stat.tweet(goalie_stat_list, goalies, abbreviations, prefix)
    print(g2)

    s3 = team_most_per.tweet(skater_stat_list, skaters, abbreviations)
    print(s3)

    g3 = team_most_per.tweet(goalie_stat_list, goalies, abbreviations)
    print(g3)
    
    
main()
