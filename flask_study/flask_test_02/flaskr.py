# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# __author__ = 'zhaojm'
# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing


# create our little application :)
app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Index Page!"



# Load default config and override config from an environment variable
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app.config.from_object(__name__)


app.config.from_envvar('FLASKR_SETTINGS', silent=True)



def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()



@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    print(entries)
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)', [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():


    error = None
    # app.logger.debug(request.form['username'])
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            # app.logger.debug('bbb')
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            # app.logger.debug('ccc')
            error = 'Invalid password'
        else:
            # app.logger.debug('ddd')
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    # app.logger.debug('eee')
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('login_in', None)
    session.clear()
    flash('You were logged out')
    # app.logger.debug()
    return redirect(url_for('show_entries'))



if __name__ == '__main__':
    app.run()
