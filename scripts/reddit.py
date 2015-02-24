#!/usr/bin/python
# -*- coding: utf-8 -*-
# get_joke needs whether to say sorry or not
# get_til needs nothing
# get_quote needs nothing

import praw


def get_joke(sorry=False):
    try:
        print 'joking'
        r = praw.Reddit(user_agent='example')
        r = r.get_random_submission('jokes')
        title = r.title
        text = r.selftext
        if sorry:
            if len(text) + 3 + len(title) > 124:
                text = text.encode('ascii', 'ignore')
                title = title.encode('ascii', 'ignore')
                return "I'm sorry you're sad. Here's a joke: \n The real joke is you"
            else:
                return "I'm sorry you're sad. Here's a joke: " + title \
                    + ((' - ' + text if len(text) != 0 else ''))
        else:
            if len(text) + 3 + len(title) > 160:
                text = text.encode('ascii', 'ignore')
                title = title.encode('ascii', 'ignore')
                return 'The real joke is you'
            else:
                return title + ((' - ' + text if len(text) != 0 else ''))
    except:
        return 'www.zombo.com'


def get_til():
    try:
        print 'TILLLL'
        r = praw.Reddit(user_agent='example')
        r = r.get_random_submission('TIL')
        title = r.title
        if len(title) > 160:
            return "TIL you're stupid"
        else:
            title = title.encode('ascii', 'ignore')
            return title
    except:
        return 'www.zombo.com'


def get_quote():
    try:
        print 'DICKENS'
        r = praw.Reddit(user_agent='example')
        r = r.get_random_submission('quotes')
        title = r.title
        if len(title) > 160:
            return 'Fuck off you maggot - Ghandi'
        else:
            title = title.encode('ascii', 'ignore')
            return title
    except:
        return 'www.zombo.com'


def do_joke(input):
    if 'joke' in input:
        return 'Valid'
    else:
        return 'Invalid'


def do_til(input):
    if 'fact' in input or 'til' in input:
        return 'Valid'
    else:
        return 'Invalid'


def do_quote(input):
    if 'quote' in input:
        return 'Valid'
    else:
        return 'Invalid'
