import web
from gothonweb import map

urls = (
	'/game','GameEngine','/','Index'
)

app = web.application(urls, globals())

#Hack so that the debug mode works with sessions
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, initializer={'room':None})
	web.config._session = session
	print("hello")
else:
	session = web.config._session


render = web.template.render("templates/", base="layout")



class Index(object):
	def GET(self):
		session.room = map.START
		web.seeother("/game")

    #def POST(self):
#	form = web.input(name="Nobody", greet="Hello")
#	greeting = "%s, %s" % (form.greet, form.name)
#	return render.index(greeting=greeting)

class GameEngine(object):
	def GET(self):
		if session.room:
			return render.show_room(room=session.room)
		else:
		#?
			return render.you_died()
	def POST(self):
		form = web.input(action=None)

		#BUG
		if (session.room and form.action):
			session.room = session.room.go(form.action)

		web.seeother("/game")

if __name__ == "__main__":
	app.run()
