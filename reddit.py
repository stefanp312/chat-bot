# get_joke needs nothing
# get_til needs nothing
# get_quote needs nothing

from random import randint
import praw

def get_joke():

    print "joking"
    r = praw.Reddit(user_agent='example')
    r = r.get_random_submission('jokes')
    title =  r.title
    text = r.selftext
    if((len(text) + 3 + len(title) )> 160):
        text = text.encode('ascii','ignore')
        title = title.encode('ascii','ignore')
        update_file("You're a joke")
        return random_joke()
    else:
        update_file(title + ( (" - " + text) if len(text) !=0 else ""))
        return random_joke()

def get_til():
    try:
        print "TILLLL"
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
        print "DICKENS"
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

def do_til(input):
    if (("fact" in input) or ("til" in input)):
        return "Valid"
    else:
        return "Invalid"


def do_quote(input):
    if "quote" in input:
        return "Valid"
    else:
        return "Invalid"
        
def update_file(joke):
    if not joke in get_file():
        file = open('jokes.txt','a')
        file.write(joke + "+++")
    else:
        print joke
        print "FDSFDSDFDS"
        
def get_file():
    file = open('jokes.txt', 'r')
    lines = file.read()
    lines2 = lines.split("+++")
    file.close()
    return lines2
    
def random_joke():
    jokes = get_file()
    return jokes[randint(0,len(jokes)-2)]