from alchemyapi import AlchemyAPI
import json
alchemyapi = AlchemyAPI()

myText = "I'm sad to get started with AlchemyAPI!"
response = alchemyapi.sentiment("text", myText)

if response['status'] == 'OK':
    print "Sentiment: ", response["docSentiment"]["type"]
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

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
