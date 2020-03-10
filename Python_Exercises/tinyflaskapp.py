# Chapter 9: Flask

from flask import Flask, abort, render_template
app = Flask(__name__)
app.debug = True

objs = __builtins__.__dict__.items()
docstrings = {name.lower(): obj.__doc__ for name, obj in objs if\
		name[0].islower() and hasattr(obj, "__name__")}

@app.route('/')
def index():
	return render_template('index.html', funcs=sorted(docstrings))
	'''link_template = '<a href="/functions/{}">{}</a></br>'
	links = []
	for func in sorted (docstrings):
		link = link_template.format(func, func)
		links.append(link)
	links_output = '\n'.join(links)
	return '<h1>Python builtins docstrings</h1>\n' + links_output
	'''
@app.route('/functions/<func_name>')
def show_docstring(func_name):
	func_name = func_name.lower()
	if func_name in docstrings:
		return render_template('docstring.html', func_name=func_name, doc=docstrings[func_name])
		'''
		output = '<h1>{}</h1>\n'.format(func_name)
		output += '<pre>{}</pre>'.format(docstrings[func_name])
		return output
		'''
	else:
		abort(404)

if __name__ == "__main__":
	app.run()
