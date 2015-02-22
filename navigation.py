import wiki.py
import twitter.py
import reddit.py

def chooseScript(bodyText=""):
	if doJoke(bodyText)=="Valid":
		getJoke(bodyText)