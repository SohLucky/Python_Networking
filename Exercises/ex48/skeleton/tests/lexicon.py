# Lexicon attempt

def split(stuff):
    stuff = raw_input('> ')
    words = stuff.split()
    return word

def check_direction(stuff):
    a = len(directions)
    for i in range(a):
	if directions[i] == stuff:
	    end.append("direction",stuff)
	else:
	    i = i + 1
    return end

def check_verb(stuff):
    a = len(verbs)
    for i in range(a):
	if verbs[i] == stuff:
	   end.append("verbs",stuff)
	else:
	    i = i + 1
    return end

def check_stop(stuff):
    a = len(stop_words)
    for i in range(a):
	if stop_words[i] == stuff:
	    end.append("stop word", stuff)
	else:
	    i = i + 1
    return end

def check_noun(stuff):
    a = len(nouns)
    for i in range(a):
	if noun[i] == stuff:
	    end.append("noun",stuff)
	else:
	    i = i + 1
    return end

def error(stuff):
    

directions = ["north", "south", "east", "west", "down", "up", "left", "right", "back"]
verbs = ["go", "stop", "kill", "eat"]
stop_words = ["the", "in", "of", "from", "at", "it"]
nouns = ["door", "bear", "princess", "cabinet"]
numbers = [0,1,2,3,4,5,6,7,8,9]
end = []
i = 0


def scan(x):
    word = split(x)
    a = len(x)
    while i < a:
	check_
	    
	    


