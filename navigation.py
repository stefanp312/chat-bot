import wiki.py
import twitter.py
import reddit.py

def choose_script(bodyText=""):
    if doJoke(bodyText) == "Valid":
        return getJoke(bodyText)
    if do_handle(bodyText) == "Valid":
        return get_handle(bodyText)
    if do_hashtag(bodyText) == "Valid":
        return get_hashtag(bodyText)
    return "Invalid"
