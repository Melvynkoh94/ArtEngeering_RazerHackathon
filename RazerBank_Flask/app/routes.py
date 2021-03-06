# Python modules
import os, logging 

# Flask modules
from flask               import render_template, request, url_for, redirect, send_from_directory
from flask_login         import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import HTTPException, NotFound, abort

# App modules
from app        import app, lm, db, bc
from app.models import User
from app.forms  import LoginForm, RegisterForm
from app.api.travels.FXRates import checkFXRates
from app.api.travels.MerchantSearch import checkMerchantSearch
from app.api.covid19 import getCovid19_WorldStats
from app.api.travels.FXRates import checkFXRates



# Test API call functionalities
print('=== API CALLS TEST ===')
# print(checkFXRates())
# print(checkMerchantSearch())
# print(getCovid19_WorldStats())

# provide login manager with load_user callback
@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Logout user
@app.route('/logout.html')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Register a new user
@app.route('/register.html', methods=['GET', 'POST'])
def register():
    
    # cut the page for authenticated users
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # declare the Registration Form
    form = RegisterForm(request.form)

    msg = None

    if request.method == 'GET': 

        return render_template( 'pages/register.html', form=form, msg=msg )

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str) 
        email    = request.form.get('email'   , '', type=str) 

        # filter User out of database through username
        user = User.query.filter_by(user=username).first()

        # filter User out of database through username
        user_by_email = User.query.filter_by(email=email).first()

        if user or user_by_email:
            msg = 'Error: User exists!'
        
        else:         

            pw_hash = password #bc.generate_password_hash(password)

            user = User(username, email, pw_hash)

            user.save()

            msg = 'User created, please <a href="' + url_for('login') + '">login</a>'     

    else:
        msg = 'Input error'     

    return render_template( 'pages/register.html', form=form, msg=msg )

# Authenticate user
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    
    # cut the page for authenticated users
    if current_user.is_authenticated:
        # checkFXRates()
        return redirect(url_for('index'))
            
    # Declare the login form
    form = LoginForm(request.form)

    # Flask message injected into the page, in case of any errors
    msg = None

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str) 

        # filter User out of database through username
        user = User.query.filter_by(user=username).first()

        if user:
            
            #if bc.check_password_hash(user.password, password):
            if user.password == password:
                login_user(user)
                return redirect(url_for('index'))
            else:
                msg = "Invalid Username or Password. Please try again."
        else:
            msg = "User not found.  Click Register to become a member."

    return render_template( 'pages/login.html', form=form, msg=msg )

# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    content = None

    try:
        # Populate Covid19 Stats Here
        print('path is: ' + path)
        if path == 'blank-page.html':
            print('Welcome to blank page!')
            periodsList = [{"Period":"Q1"}, {"Period":"Q2"}, {"Period":"Q3"}, {"Period":"Q4"}]
            return render_template('pages/'+path, msg=msg, periodsList=periodsList)

        if path == 'fxrates.html':
            fxrates_response = checkFXRates(156, 702)
            print(fxrates_response)
            print("Going to " + "pages/"+path)
            return render_template('pages/'+path, fxrates_response=fxrates_response)


        # try to match the pages defined in -> pages/<input file>
        return render_template( 'pages/'+path )
    
    except:      
        return render_template( 'pages/error-404.html' )


@app.route('/fxrates_form', methods=['POST'])
def fxrates_form():
    # Get URL parameters based on destination code, and country code
    req = request.form
    destinationCode = req.get("destinationCode")
    sourceCode = req.get("sourceCode")
    
    fxrates_response = checkFXRates(destinationCode, sourceCode)
    print(fxrates_response)
    return render_template('pages/'+path, fxrates_response=fxrates_response)


# Return sitemap 
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml')
