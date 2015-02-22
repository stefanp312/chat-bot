import wiki
import reddit
import twitter

def choose_script(bodyText=""):
    bodyText = bodyText.lower()
    if reddit.do_joke(bodyText) == "Valid":
        return reddit.get_joke()
    elif reddit.do_til(bodyText) == "Valid":
        return reddit.get_til()
    elif reddit.do_quote(bodyText) == "Valid":
        return reddit.get_quote()
    elif twitter.do_handle(bodyText) == "Valid":
        return twitter.get_handle(bodyText)
    elif twitter.do_hashtag(bodyText) == "Valid":
        print bodyText
        text = twitter.get_hashtag(bodyText)
        print text
        return text
        return twitter.get_hashtag(bodyText)
    elif wiki.willsearch(bodyText) == "Valid":
        return wiki.searchwikipedia(bodyText)
    return "Invalid"
