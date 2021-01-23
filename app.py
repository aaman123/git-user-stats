from flask import Flask , render_template , request, redirect, url_for
from flask_bouncer import requires, ensure, Bouncer

import csv

# from repos.api import get_user
# from repos.exceptions import GitHubApiException

app = Flask(__name__)
bouncer = Bouncer(app)


selected_users = ['aaman123']

@bouncer.authorization_method
def define_authorization(user, they):
    if user.is_admin:
        they.can(MANAGE, ALL)
    else:
        they.can(login, ('Article', 'BlogPost'))


@app.route("/" , methods = ['GET', 'POST'])
def index():
    return render_template("register.html")

@app.route("/login" , methods = ['GET', 'POST'])
def login():
    return render_template("login.html")




@app.route('/welcome',methods = ['GET','POST'])
@requires(login,login)
def welcome():
    return render_template("welcome.html")

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "GET":
        return redirect(url_for('index'))
    elif request.method == "POST":
        userdata = dict(request.form)
        name = userdata["name"]
        email = userdata["email"]
        password = userdata["password"]
        if len(name) < 2 and len(email) < 3 and (len(password) < 10):
            return "Please submit valid data."
        with open('data/data.csv', mode='a') as csv_file:
            data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data.writerow([name,email,password])
    return redirect(url_for('login'))

@app.route("/afterlogin", methods=["GET", "POST"])
def afterlogin():
    if request.method == "GET":
        return redirect(url_for('index'))
    elif request.method == "POST":
        login = False
        first_line = True
        userdata = dict(request.form)
        name = userdata["name"]
        print(name)
        email = userdata["email"]
        print(email)
        password = userdata["password"]
        print(password)
        user_data = []
        with open('data/data.csv', mode='r') as csv_file:
            data = csv.reader(csv_file, delimiter=',')
            for row in data:
                print(row)
                if name and email and password not in row:
                    return "please enter valid data"
                else:
                    return "user logged in successfully"
                break
    return redirect(url_for('login'))





    

    # results = get_user(users)

    # return render_template(
    #     'index.html',
    #     # results = results
       
     
# @app.route("/register" , methods = ['GET', 'POST'])
# def register():
#     username = request.args.get('name')
#     email = request.args.get('email')
#     password = request.get('password')
#     if username and email:
#         new_user = User(
#             username=username,
#             email=email,
#             password = password,
#             created=dt.now(),
#             bio="In West Philadelphia born and raised, \
#             on the playground is where I spent most of my days",
#             admin=False
#         )
#         db.session.add(new_user)  # Adds new User record to database
#         db.session.commit()  # Commits all changes
#     return make_response(f"{new_user} successfully created!")
#     return render_template('register.html')
    
# @app.errorhandler(GitHubApiException)

# def handle_error(error):
#     return render_template('error.html' , message = error)