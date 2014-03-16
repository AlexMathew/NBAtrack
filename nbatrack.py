"""
	nbatrack.py
	Given a particular date, reads the scores page for the day and gives a list of games from that day.
"""

import urllib
import datetime
from bs4 import BeautifulSoup as Soup

def _read_page(link):
	u = urllib.urlopen(link)
	text = u.read()
	return text	

def _format_link(day):
	link = ["http://scores.espn.go.com", "/nba", "/scoreboard", "?date="]
	link.append(day.strftime("%Y%m") + str(int(day.strftime("%d")) - 1))
	scoreboard_link = "".join(link)
	return scoreboard_link

def matchday():
	day = datetime.datetime.now()
	day_page = _read_page(_format_link(day))
	