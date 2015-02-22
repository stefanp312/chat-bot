from alchemyapi import AlchemyAPI
import reddit
import twitter
import wiki
import Introduction

def process_text(query=""):
    alchemyapi = AlchemyAPI()
    response2 = alchemyapi.sentiment("text", query)
    # term list for natural language keyword analysis
    jokes_term_list = ["jokes", "joke", "tell me a joke", "funny joke", "humor me", "humor", "make me laugh", "laugh", "pun", "one liner", "smartass"]
    search_term_list = ["search", "where", "when was", "when did", "who is", "why", "who was", "when was", "tell me about", "what is", "tell", "how does", "what makes", "question", "wikipedia", "how to", "find", "wat is", "wat makes", "wut is"]
    twitter_term_list = ["tweet", "twitter", "#", "hashtag", "funny tweet", "updates about"]
    name_term_list = ["your name", "ur name", "youre name", "wat are you", "what are you", "who are you"]
    salute_term_list = ["hi", "hello", "how are you", "good morning", "sup", "good evening", "goodnight", "hey", "salut", "bonjour", "what's up", "goodbye", "bye"]
    til_term_list = ["fact", "til", "learn", "cool facts"]

    if response2['status'] == 'OK':

        print "Sentiment: ", response2["docSentiment"]["type"]
        print('## Response Object ##')
        response = alchemyapi.combined("text", query)
        print response
        print('')

        print('## Keywords ##')
        for keyword in response['keywords']:
            print(keyword['text'], ' : ', keyword['relevance'])
        print('')

        print('## Concepts ##')
        for concept in response['concepts']:
            print(concept['text'], ' : ', concept['relevance'])
        print('')

        print('## Entities ##')
        for entity in response['entities']:
            print(entity['type'], ' : ', entity['text'], ', ', entity['relevance'])
        print(' ')

    else:
        print('Error in combined call: ', response['statusInfo'])

    for term in name_term_list:
        if term in query.lower():
            print "name stuff"
            return Introduction.give_name()
    for term in salute_term_list:
        if term in query.lower():
            print "hi stuff"
            return Introduction.salute(term)
    for term in til_term_list:
        if term in query.lower():
            print "til reddit"
            return reddit.get_til()
    for term in jokes_term_list:
        if term in query.lower():
            print "jokes"
            return reddit.get_joke(False)
    for term in search_term_list:
        if term in query.lower():
            for keyword in response['keywords']:
                print "wikipedia search"
                print keyword['text']
                return wiki.searchwikipedia(keyword['text'])
    for term in twitter_term_list:
        if term in query.lower():
            for keyword in response['keywords']:
                print "twitter"
                return twitter.get_hashtag(keyword['text'])
    if response2["docSentiment"]["type"].lower() == "negative":
        print "I'm sorry you're sad. Here's a joke."
        return reddit.get_joke(True)
    return twitter.get_hashtag(query)