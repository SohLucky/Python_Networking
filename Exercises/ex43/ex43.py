from sys import exit
from random import randint

class Scene(object):
	def enter(self):
		print ("scene")
		return

class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print ("\n----------------")
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
	quips = [
		"You died. You kinda suck at this.",
		"Your mum would be proud---if she were smarter",
		"Take the L"
		]
	def enter(self):
		print (Death.quips[randint(0, len(self.quips)-1)])
		exit()

class CentralCorridor(Scene):
	def enter(self):
		print ("The Gothans of Planet Percal 25 have invaded your ship and destroyed")
		print ("your entire crew. You are the last surviving member and your last mission")
		print ("Blah Blah Blah")
		action = raw_input("> ")

		if action == "shoot":
			print ("Quick on the draw and yank out your blaster and fire it at the Gothan.")
			print ("Deaded")
			return "death"
		elif action == "dodge":
			print ("Why are you running away?")
			return "death"
		elif action == "tell a joke":
			print ("You think you very funny")
			return "laser_weapon_armory"
		else:
			print ("Does Not Compute")
			return 'central_corridor'

class LaserWeaponArmory(Scene):
	def enter(self):
		print ("Ypi do a dive roll into the Weapon armory, crouch and scan the room for any buggers that might stillbe hiding")
		print ("You found a neutron bomb in its container and there is a ketypad lock onthe bos and you need the code to defuse it.")
		print ("the code is 3 digits")
		code = "%d%d%d" % (1,2,3)
		guess = raw_input("> ")
		guesses = 0

		while guess != code and guesses <10:
			print ("BZZZZED")
			guesses += 1
			guess = raw_input("> ")
		if guess == code:
			print ("THe container clicks open adn the seal breaks, letting gas out.You grab the neturon bomb and throw it as far away as you can")
			return "the_bridge"

		else:
			print ("The lock buzzes one last time and then tyou hear a sickening melting sound")
			return "death"
class TheBridge(Scene):
	def enter(self):
		print ("You burst onto the bridege with the neutron destruct bomb")
		print ("under your arm and surprise 5 gothan who are trying to take control of the ship.")
		print ("DO you want to throw thw bomb or slowly place the bomb")
		action = raw_input("> ")

		if action == "throw the bomb":
			print ("In a panic you threw the bomb aaway and it goes off in your face.")
			return "death"

		elif action == "slowly place the bomb":
			print ("you successfully placed the bomb in a location far from you.")
			return 'escape_pod'

class EscapePod(Scene):
	def enter(self):
		print ("You rush through the ship desperately truing to make it to the escape pod before the whole ship exlodes.")
		good_pod = 5
		guess = raw_input("[pod no.]> ")

		if int(guess) == good_pod:
			print ("You jumped into the good pod and hit the eject button")
			print ("You escaped this god forsaken planet and win the game")
			return "finished"
		else:
			return "death"

class Finished(Scene):
	def enter(self):
		print ("Good Job in completing the game!\nYou survived!")
		exit()
class Map(object):
	scenes = {
		"central_corridor":CentralCorridor(),
		"laser_weapon_armory":LaserWeaponArmory(),
		"the_bridge":TheBridge(),
		"escape_pod":EscapePod(),
		"death":Death(),
		"finished":Finished()
		}
	def __init__(self, start_scene):
		self.start_scene = start_scene
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
