from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
'''
Importing Flask class from flask. Creating app variable and setting instance of Flask class.
__name__ is the name is a special variable in python which is juste the name of the module.
'''
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b7be5ac39d0bed1d385696f201e00ad5'

posts = [
    {
        'author': 'Ishan Ohri',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'Feb 09,2020',
    },
    {
        'author': 'Anish Ohri',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'Feb 05,2020'
    }
]

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__=='__main__':
    app.run(debug=True)