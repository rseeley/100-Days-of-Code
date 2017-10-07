from flask import Flask, request, make_response, render_template, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)


@app.route('/')
def index():
    resp = make_response(render_template())
    resp.set_cookie('username', 'the username')
    username = request.cookies.get('username')
    return 'Index Page'


@app.errorhandler(404)
def not_found(error):
    resp = make_response('page_not_found.html'), 404
    resp.headers['X-Something'] = 'A value'
    return resp


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


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))
