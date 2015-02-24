from flask import Flask, request, redirect, session
import twilio.twiml
import navigation

SECRET_KEY = 'donuts'
logging = True
app = Flask(__name__)
app.config.from_object(__name__)


def log(mesagge=""):
    if logging:
        print mesagge


@app.route("/", methods=['GET', 'POST'])
def main_reply():
    # Log values from request
    from_number = request.values.get('From', None)
    log(from_number)
    recieved_message = request.values.get('Body')
    log(recieved_message)
    # pick reply to message
    reply = navigation.choose_script(bodyText=recieved_message)
    # trim the length of the reply to one text
    if len(reply) > 160:
        reply = reply[0:159]
    if reply == "":
        reply = "Error."

    # get the response scheme from twilio and add reply as message body
    resp = twilio.twiml.Response()
    resp.message(reply.encode("utf-8"))
    # log server reply
    log(reply)
    # store previous queries of the user in a cookie
    searchs = session.get('searchs', [])
    searchs.append(recieved_message)
    replies = session.get('searchs', [])
    replies.append(reply)
    # Save the new cmds/searchs list in the session
    session['searchs'] = searchs

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
