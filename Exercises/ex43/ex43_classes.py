#Exercise 43

class Scene(object):
	def enter(self):
		pass

class Engine(object):
	def __init__(self, scene_map):
		pass
	def plat(self):
		pass

class Death(Scene):
	def enter(self):
		pass

class CentralCorridor(Scene):
	def enter(self):
		pass

class LaserWeaponArmory(Scene):
	def enter(self):
		pass

class TheBridge(Scene):
	def enter(self):
		pass

class EscapePod(Scene):
	def enter(self):
		pass



a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()
