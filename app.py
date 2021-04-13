from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "caninputwhateversecretkeyyouwant"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class contact_form(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column('name', db.String(50))
    email = db.Column('email', db.String(100))
    message = db.Column('message', db.String(255))

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

class login(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(20))
    password = db.Column("password", db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        firstname = request.form["first_name"]
        lastname = request.form["last_name"]
        email = request.form['email']
        message = request.form['msg']
        if firstname != "" or lastname != "" or email != "" or message != "" :
            contactNow = contact_form(firstname+' '+lastname, email, message)
            db.session.add(contactNow)
            db.session.commit()
            flash("We appreciate you reaching out to us!", "info")
        else:
            flash("Sorry Empty fields!", "danger")

    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio-page.html')

@app.route('/portfolioII')
def portfolioII():
    return render_template('portfolioII-page.html')

@app.route('/dashboard')
def dashboard():
    if "user" in session:
        unm = session['user']
        return render_template('dashboard.html',username=unm, values=contact_form.query.all())
    else:
        return redirect(url_for('admin'))

@app.route('/admin', methods = ['POST', 'GET'])
def admin():
    # db.session.query(contact_form).delete()
    # db.session.commit()
    if "user" in session:
        unm = session['user']
        return render_template('dashboard.html',username=unm, values=contact_form.query.all())
        
    if request.method == "POST":
        session.permanent = True

        usrnm = request.form["username"]
        ps = request.form["password"]
        
        found_user = login.query.filter_by(username = usrnm, password = ps).all()
        if found_user:
            session["user"] = usrnm
            return redirect(url_for("dashboard"))
        else:
            flash("Sorry! You entered wrong details.", "danger")

    return render_template('login.html')

@app.route('/logout')
def logout():
    if "user" in session:
        u = session["user"]
        flash("You were logged out", "info")
    session.pop("user", None)
    return redirect(url_for("admin"))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
    
