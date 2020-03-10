# Lexicon attempt
#! /usr/bin/python
import sys

directions=["north", "south", "east", "west", "down", "up", "left", "right", "back"]
verbs = ["go", "stop", "kill", "eat"]
stop_words = ["the", "in", "of", "from", "at", "it"]
nouns = ["door", "bear", "princess", "cabinet"]
numbers = [0,1,2,3,4,5,6,7,8,9]
i = 0
end = []

def check_word(stuff):
    checker = 0
#Check for direction word
    a = len(directions)
    for i in range(a):
	if directions[i] == stuff:
	    end.append(["direction",stuff])
	    checker = 1
	    break
	else:
	    checker = 0
#Check for verb
    a = len(verbs)
    if checker != 1:
	for i in range(a):
	    if verbs[i] == stuff:
	        end.append(["verbs",stuff])
	        checker = 1
	        break
	    else:
	        checker = 0
#Check for stop word
    a = len(stop_words)
    if checker != 1:
	for i in range(a):
	    if stop_words[i] == stuff:
	        end.append(["stop word", stuff])
	        checker = 1
	        break
	    else:
	        checker = 0

#Check for noun word
    a = len(nouns)
    if checker != 1:
	for i in range(a):
	    if nouns[i] == stuff:
	        end.append(["noun",stuff])
	        checker = 1
	        break
	    else:
	        checker = 0
#Check for integer
    if checker != 1:
	try:
	    int(stuff)
	    end.append(["number",stuff])
	    checker =1
	except ValueError:
	    checker = 0

#Check for error word
    if checker == 0:
	end.append(["error", stuff])
    else:
	return end

def scan(x):
    global end
    word = x.split()
    a = len(word)
    for i in range(a):
        check_word(word[i])
	i = i + 1
    print(end)
    end*=0
