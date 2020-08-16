from flask import render_template, url_for, flash, redirect
from flask_blog import app
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post


posts = [
    {
        'author': 'John Quick',             # Dictionary entries displayed/passed into
        'title' : 'Blog post 1',            # templates by passing an argument with our data
        'content': 'First post content',    # 
        'date_posted': 'August 67, 2056'    #
    },
    {
        'author': 'Munchma Quchi',
        'title' : 'Blog post deux',
        'content': 'Second post content',
        'date_posted': 'August 68, 2056'
    }
]

@app.route('/')
@app.route('/home')
def home():                                             # "posts=posts" = argument which accepts the above dictionary entries
    return render_template('home.html', posts=posts)    # posts variable = posts [] 

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful.  Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)