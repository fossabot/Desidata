from flask import Flask, render_template, request
import config

# Initializing flask
app = Flask(__name__)


@app.route('/')  # Index route
def index():
    '''
            Routes to index.html - homepage
    '''
    return render_template('index.html')


@app.route('/search')
def search():
    '''
            Renders search.html
            TODO : Find Better solution to it.
                    1. Use HTML input box for better UX.
    '''
    return render_template('profile.html')


@app.route('/state/<state>')
def go_state(state):
    '''
            Renders state specific HTML page
    '''
    if state in state_dictionary:
        return render_template(state+'.html')
    else:
        return render_template('error.html')

@app.route('/test')
def test_vix():
    path = "./static/js/viz/india/census/test.html"
    return app.send_static_file(path)

@app.route('/india')
def go_india():
    '''
                    Renders India page
    '''
    return render_template('india.html', title="India")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
