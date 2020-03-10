class Room(object):
    def __init__(self,name, description):
	self.name = name
	self.description = description
	self.paths = {}

    def go(self, direction):
	return self.paths.get(direction, None)

    def add_paths(self, paths):
	self.paths.update(paths)

central_corridor = Room("Central Corridor",
'''
The Gothans of planet percal have invaeded your ship and destoryed your entire crew. You are the last surviving meme  and your last mission is to get the neutron destruct bomb from the weapons armory and put it inth briege and blow the ship ip agter getting into an escape pod.
You are running down the central corridor tothwe apons armoury when a gothan jumps out. He's blocking ht edoor to the armory and is about to pull a weapon to blask you.
'''
)

laser_weapon_armory = Room("Laser Weapon Armory", 
'''
Lucky for you they learn gothans insults in the academy. You tell the one gothan joke you know. Blah blah blah
You do a dive troll into the weapon armory, crouch and scan the room for more gothans that might be hiding. There is a keypad on the box and you need the code to get the bomb out, If you get th code wrong 1- times, the lock closes forever and you can;t get th bomb. THe code is 3 digit
'''
)

the_bridge = Room("The Bridge" ,
'''
THe container clicks open and the seal breaks, letting gas out off your buttocks. 
You grab the neutron om b and run for your life.
Blah Blah Blah
'''
)

escape_pod = Room("Escape Room", 
'''You point your blaster at the bomb under your arm and the gothans put their hands up and start to sweat. YOu inch backwards towards the door adr open it. 
You want to escape and there is only 5 pods. Which one do you take
'''
)

the_end_winner = Room("The End", 
'''
YOu jumpp into pod 2 and hit the eject button.
The pod easily slides out into the speac heading to the planet below. As it flies to the planet, you look back and see tyour ship implode then explode like bright star, taking out he GOthan ship at the same time, YOu won!
'''
)

the_end_loser = Room("The End",
'''
You jump into a random pod and hit the eject button
the Pod esapes out into the void of space and the you dead, cause you suck:)
'''
)

escape_pod.add_paths({'2':the_end_winner, '*':the_end_loser})

generic_death = Room("death", "You died")

the_bridge.add_paths({'throw the bomb':generic_death, 'slowly place the bomb':escape_pod})

laser_weapon_armory.add_paths({'0132':the_bridge,'*':generic_death})

central_corridor.add_paths({'shoot':generic_death,'dodge':generic_death, 'tell a joke':laser_weapon_armory})

START = central_corridor
