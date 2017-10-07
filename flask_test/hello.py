from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

@app.route('/user/<username>')
def show_user_profile(username):
	# show the user profile for that user
	return f'User {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
	# show the post with the given id, the id is an integer
	return f'Post {post_id}'

@app.route('/projects/')
def projects():
	return 'The project page'

@app.route('/about')
def about():
	return 'The about page'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
# 	if request.method == 'POST':
# 		do_the_login()
# 	else:
# 		show_the_login_form()

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)
	