
#Random Password Generator

import random
import string

list = []
final = []
lowalph = string.ascii_lowercase
uppalph = string.ascii_uppercase


upper = int(input("Enter the number of CAPS character to be in password: "))
lower = int(input("Enter the number of lower character to be in password: "))
num = int(input("Enter number of numbers to be in pw: "))
total = upper + lower + num

while len(final) < total:
	for x in range(0, upper):
		final.append(random.choice(uppalph))
	for x in range(0, lower):
		final.append(random.choice(lowalph))
	for x in range(0, num):
		final.append(random.choice(string.digits))
random.shuffle(final)
print("".join(final))

