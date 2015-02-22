import wiki.py
import twitter.py
import reddit.py

def choose_script(bodyText=""):
    if doJoke(bodyText) == "Valid":
		getJoke(bodyText)
	if do_handle(bodyText) == "Valid":
		get_handle(bodyText)
	if do_hashtag(bodyText) == "Valid":
		get_hashtag(bodyText)