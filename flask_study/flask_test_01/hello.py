from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	return "Index Page!"

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)
#
#
# #
# @app.route('/user/<username>')
# def show_user_profile(username):
#     return 'User %s' % username
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return 'Post %d' % post_id
#
#
# @app.route('/projects/')
# def projects():
#     return 'The project page'
#
# @app.route('/about')
# def about():
#     return 'The about page'

if __name__ == "__main__":
    # app.debug = True
	app.run()

