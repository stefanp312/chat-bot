# get_hashtag needs the text
# get_handle needs the text

from twython import Twython

def get_hashtag(tag):
    try:
        print "##############################"
        APP_KEY = 'MDszGMPdCSC6ujOVB86YXwwMX'
        ACCESS_TOKEN = "AAAAAAAAAAAAAAAAAAAAAMNpeQAAAAAAzW0NtAlnkRbxa%2FvGJc2iKxoz8oM%3DVjIzeLDaWXBPybTv8mKRlXgDoQWbQW56ZbM4xcxk5yPRlBXsQs"
        print "##############################"
        twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
        if(tag[0] != '#'):
            tag = '#' + tag
        print "##############################"
        
        results = twitter.search(q=tag, result_type='recent', lang="en",count=1)
        print results
        print "##############################"
        results = results[results.keys()[1]][0]
        result = results[results.keys()[2]]
        result = result.encode('ascii','ignore')
        return result
    except:
        return "www.zombo.com"


def get_handle(handle):
        try:
            print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            APP_KEY = 'MDszGMPdCSC6ujOVB86YXwwMX'
            ACCESS_TOKEN = "AAAAAAAAAAAAAAAAAAAAAMNpeQAAAAAAzW0NtAlnkRbxa%2FvGJc2iKxoz8oM%3DVjIzeLDaWXBPybTv8mKRlXgDoQWbQW56ZbM4xcxk5yPRlBXsQs"

            twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

            if(handle[0] != '@'):
                handle = '@' + handle

            results = twitter.search(q=handle, result_type='recent', lang="en",count=1)

            results = results[results.keys()[1]][0]
            result = results[results.keys()[2]]
            result = result.encode('ascii','ignore')
            return result
        except:
            return "www.zombo.com"


def do_handle(input):
    if "@" in input:
        return "Valid"
    else:
        return "Invalid"

def do_hashtag(input):
    if "#" in input:
        return "Valid"
    else:
        return "Invalid"

