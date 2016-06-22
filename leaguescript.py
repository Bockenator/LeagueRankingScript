from riotwatcher import RiotWatcher
from riotwatcher import EUROPE_WEST
import operator
#Your API key here
w = RiotWatcher('')

if w.can_make_request():
	dict = {}
	num_players = input('How many players are we comparing?\n')
	for x in range(0, num_players):
		player_name = raw_input('Enter player name\n')
		player = w.get_summoner(name = player_name, region = EUROPE_WEST)
		#Hihgly complex algorithm designed to predict a players ability to play legaue
		dict[player['name']] = player['id']/player['profileIconId'] + player['revisionDate']/player['id']
	sortDic = sorted(dict.items(), key=operator.itemgetter(1))
	print "The best player is:\n"
	print dict.keys()[0]
else:
	print "You aren't allowed to"
