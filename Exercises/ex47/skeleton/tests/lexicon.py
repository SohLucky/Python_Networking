# Lexicon attempt

stuff = raw_input('> ')
words = stuff.split()

directions = =[north, south, east, west, down, up, left, right, back]
verbs = [go, stop, kill, eat]
stop_words = [the, in, of, from, at, it]
nouns = [door, bear, princess, cabinet]
numbers = [0,1,2,3,4,5,6,7,8,9]

def token(error):
    if error = True:
        print("User input is messed up")
    else:
        continue

def convert_numeber(s):
    try:
	return int(s)
    except ValueError:
	return None

