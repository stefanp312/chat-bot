# get_hashtag needs the text
# get_handle needs the text

from twython import Twython
import json

def get_hashtag(tag):
    
    try:
        APP_KEY = 'MDszGMPdCSC6ujOVB86YXwwMX'
        ACCESS_TOKEN = "AAAAAAAAAAAAAAAAAAAAAMNpeQAAAAAAzW0NtAlnkRbxa%2FvGJc2iKxoz8oM%3DVjIzeLDaWXBPybTv8mKRlXgDoQWbQW56ZbM4xcxk5yPRlBXsQs"
        print "#############################cxfsfgvvxgfd#"
        twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
        if(tag[0] != '#'):
            tag = '#' + tag

        
        results = twitter.search(q=tag, result_type='recent', lang="en",count=1)


        keys = results.keys()
        key = ""
        if "status" in keys[0]:
            key = keys[0]
        else:
            key = keys[1]  
        result = results[key]
        text = result[0]['text']
        return text.encode("utf-8")
    except:
        return "www.zombo.com"

def get_handle(handle):
        try:
            APP_KEY = 'MDszGMPdCSC6ujOVB86YXwwMX'
            ACCESS_TOKEN = "AAAAAAAAAAAAAAAAAAAAAMNpeQAAAAAAzW0NtAlnkRbxa%2FvGJc2iKxoz8oM%3DVjIzeLDaWXBPybTv8mKRlXgDoQWbQW56ZbM4xcxk5yPRlBXsQs"

            twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

            if(handle[0] != '@'):
                handle = '@' + handle

            results = twitter.search(q=handle, result_type='recent', lang="en",count=1)

            keys = results.keys()
            key = ""
            if "status" in keys[0]:
                key = keys[0]
            else:
                key = keys[1]  
            result = results[key]
            text = result[0]['text']
            return text.encode("utf-8")
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

