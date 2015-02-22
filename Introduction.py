
# name_term_list=["your name","ur name","youre name"]
# salute_term_list=["hi","hello","how are you","good morning","sup","good evening","goodnight","goodnight"]
from random import randint

def salute(keyword):
	try:
		bye_term_list = ["good evening", "goodnight", "goodnight"]
		if keyword in bye_term_list:
			return "Goodbye!"
		else:
			i = randint(1, 9)
			if i == 1:
				return "Top of the morning to ya!"
			elif i == 2:
				return "Hey pal!"
			elif i == 3:
				return "What's cookin' good lookin'?"
			elif i==4:
				return "HI! I AM EXCITED TO TALK TO YOU"
			elif i==5:
				return "G'day mate"
			elif i==6:
				return "Sup dawg \n (\"up dawg\"...\"what's up dawg?\")"
			elif i==7:
				return "Well hello there :)"
			elif i==8:
				return "Hey, baby, won't you look my way?\nI can be your new addiction\nHey, baby, what you gotta say?\nAll you're giving me is fiction"
			else:
				return "Well aren't you a social butterfly, approaching me like that!"
	except:
		return "Invalid"
		
def give_name():
	try:
		return "My name is Jonas!\nhttp://youtu.be/VoAnLHSLHGQ\n#weezer"
	except:
		return "Invalid"

def what_do():
	try:
		return "I am chatbot that can search twitter, wikipedia, reddit, with natural language processing."
	except:
		return "Invalid"

print salute("Hi")