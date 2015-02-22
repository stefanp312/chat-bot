import wiki
import twitter
import reddit

def choose_script(bodyText=""):
    if reddit.doJoke(bodyText) == "Valid":
        return reddit.getJoke(bodyText)
    elif twitter.do_handle(bodyText) == "Valid":
        return twitter.get_handle(bodyText)
    elif twitter.do_hashtag(bodyText) == "Valid":
        return twitter.get_hashtag(bodyText)
    elif wiki.willsearch(bodyText) == "Valid":
        return wiki.searchwikipedia(bodyText)
    return "Invalid"
