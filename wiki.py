import wikipedia

def willsearch(bodyText=""):
    if "search" in bodyText:
		return "Valid"
    return "Invalid"

def searchwikipedia(query, sentences=1):
    summary = ""
    try:
        summary = wikipedia.summary(query, sentences=sentences)
    except wikipedia.exceptions.DisambiguationError as e:
        # + ", ".join(e.options)
        summary = wikipedia.summary(e.options[1], sentences=sentences)
    return summary

if __name__ == "__main__":
    main()
