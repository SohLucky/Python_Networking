# Challenge 372 [Easy] Perfectly Balanced
from collections import Counter

total_x = 0
total_y = 0

def balanced(word):
	global total_x
	global total_y
	split_word = list(word)
	for a in range (len(split_word)):
		if "x" == split_word[a]:
			total_x += 1
		elif "y" == split_word[a]:
			total_y += 1
		else:
			continue
	if total_x == total_y:
		print("True")
	else:
		print("False")

def balanced_bonus(word):
	split_dict = Counter(word)
	empty_check = not bool(split_dict)
	if empty_check == False:
		first_value = list(split_dict.values())[0]
		for v in range (len(split_dict.values())):
			if first_value ==  list(split_dict.values())[v]:
				continue
			else:
				print("False")
				return
	else:
		print("True")
	print("True")
#balanced("xxxyyy")
#balanced("xxxy")
#balanced("")
#balanced("x")
balanced_bonus("hello")
balanced_bonus("xxyy")
balanced_bonus("xyz")
#balanced_bonus("")

