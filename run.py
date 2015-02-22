from flask import Flask, request, redirect, session
import twilio.twiml
import wikipedia

SECRET_KEY = 'donuts'
app = Flask(__name__)
app.config.from_object(__name__)

# Try adding your own number to this list!

@app.route("/", methods = ['GET', 'POST'])
def main_reply():
    from_number = request.values.get('From', None)
    print from_number
    recieved_message = request.values.get('Body')

    # create cmds variable from cookies
    cmds = session.get('cmds', [""])
    searchs = session.get('searchs', [["", 0]])

    reply = searchwikipedia(query=recieved_message)
    
    # trim the length of the reply to one text
    if len(reply) > 160:
        reply = reply[0:159]

    # get the response scheme from twilio and add reply as message body
    resp = twilio.twiml.Response()
    resp.message(reply)

    print reply

    # Save the new cmds/searchs list in the session
    session['cmds'] = cmds
    session['searchs'] = searchs

    return str(resp)

def searchwikipedia(query, sentences=1):
    summary = ""
    try:
        summary = wikipedia.summary(query, sentences=sentences)
    except wikipedia.exceptions.DisambiguationError as e:
        # + ", ".join(e.options)
        summary = wikipedia.summary(e.options[1], sentences=sentences)
    return summary

if __name__ == "__main__":
    app.run(debug=True)
