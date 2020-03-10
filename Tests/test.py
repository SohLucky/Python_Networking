from sys import argv

script , user_name, filex = argv

prompt = raw_input("User Input: ")

text = open(filex)

print("I am script %s " % script)
print("My Username is %s " % user_name)
print("Stop typing %s " % prompt)
print("Contents of your file %s is " % filex)
print(text.read())
