import wiki
import reddit
import twitter
import testNat

def choose_script(bodyText=""):
    bodyText = bodyText.lower()
    if reddit.do_joke(bodyText) == "Valid":
        return reddit.get_joke(False)
    if reddit.do_til(bodyText) == "Valid":
        return reddit.get_til()
    if reddit.do_quote(bodyText) == "Valid":
        return reddit.get_quote()
    if twitter.do_handle(bodyText) == "Valid":
        return twitter.get_handle(bodyText)
    if twitter.do_hashtag(bodyText) == "Valid":
        return twitter.get_hashtag(bodyText)
    if wiki.willsearch(bodyText) == "Valid":
        return wiki.searchwikipedia(bodyText)
    return testNat.process_text(bodyText)

