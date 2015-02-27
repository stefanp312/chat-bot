import wikipedia


def willsearch(body_text=""):
    if "search" in body_text:
        return "Valid"
    return "Invalid"


def searchwikipedia(query, sentences=1):
    summary = ""

    if "search" in query[0:10]:
        query = query[7:]
        print query

    try:
        summary = wikipedia.summary(query, sentences=sentences)
    except wikipedia.exceptions.DisambiguationError as e:
        # + ", ".join(e.options)
        summary = wikipedia.summary(e.options[1], sentences=sentences)
    return summary.encode("utf-8")

if __name__ == "__main__":
    searchwikipedia("")
