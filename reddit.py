# get_joke needs nothing
# get_til needs nothing
# get_quote needs nothing

import praw

def get_joke():
    try:
        r = praw.Reddit(user_agent='example')
        r = r.get_random_submission('jokes')
        title =  r.title
        text = r.selftext
        if((len(text) + 3 + len(title) )> 160):
            text = text.encode('ascii','ignore')
            title = title.encode('ascii','ignore')
            return "Your a joke"
        else:
            return title + ( (" - " + text) if len(text) !=0 else "")
    except:
        return "www.zombo.com"
def get_til():
    try:
        r = praw.Reddit(user_agent='example')
        r = r.get_random_submission('TIL')
        title =  r.title
        if((len(title))> 160):
            return "TIL you're stupid"
        else:
            title = title.encode('ascii','ignore')
            return title
    except:
        return "www.zombo.com"
def get_quote():
    try:
        r = praw.Reddit(user_agent='example')
        r = r.get_random_submission('quotes')
        title =  r.title
        if((len(title))> 160):
            return "Fuck off you maggot - Ghandi"
        else:
            title = title.encode('ascii','ignore')
            return title
    except:
        return "www.zombo.com"
def do_joke(input):
    if "joke" in input:
        return "Valid"
    else:
        return "Invalid"

def do_til():
    if "fact" in input:
        return "Valid"
    else:
        return "Invalid"


def do_quote():
    if "quote" in input:
        return "Valid"
    else:
        return "Invalid"
