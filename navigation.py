import wiki
import reddit
import twitter

def choose_script(bodyText=""):
    if reddit.do_joke(bodyText) == "Valid":
        return reddit.get_joke(bodyText)
    elif twitter.do_handle(bodyText) == "Valid":
        return twitter.get_handle(bodyText)
    elif twitter.do_hashtag(bodyText) == "Valid":
        return twitter.get_hashtag(bodyText)
    elif wiki.willsearch(bodyText) == "Valid":
        return wiki.searchwikipedia(bodyText)
    return "Invalid"