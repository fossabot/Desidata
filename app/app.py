from flask import Flask, render_template, request
import config

# Initializing flask
app = Flask(__name__)


@app.route('/')  # Index route
def index():
    '''
            Routes to index.html - homepage
    '''
    return render_template('index.html', 200)


@app.route('/search')
def search():
    '''
            Renders search.html
            TODO : Find Better solution to it.
                    1. Use HTML input box for better UX.
    '''
    return render_template('search.html', 200)


@app.route('/state/<state>')
def go_state( < state > ):
    '''
            Renders state specific HTML page
    '''
    if state in state_dictionary:
		return render_template( < state > +'.html' , 200)
	else:
		return render_template('error.html' , 200)

@app.route('/india')
def go_india():
	'''
			Renders India page
	'''
	return render_template('india.html' , 200)

