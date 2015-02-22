import wiki
import reddit
import twitter

def choose_script(bodyText=""):
    print bodyText
    if reddit.doJoke(bodyText) == "Valid":
        print reddit.getJoke(bodyText)
        return reddit.getJoke(bodyText)
    elif twitter.do_handle(bodyText) == "Valid":
        print twitter.get_handle(bodyText)
        return twitter.get_handle(bodyText)
    elif twitter.do_hashtag(bodyText) == "Valid":
        print twitter.get_hashtag(bodyText)
        return twitter.get_hashtag(bodyText)
    elif wiki.willsearch(bodyText) == "Valid":
        print wiki.searchwikipedia(bodyText)
        return wiki.searchwikipedia(bodyText)
    return "Invalid"
