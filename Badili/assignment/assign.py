from flask import Flask, render_template , url_for, request , redirect , flash
from dbc import dbconnect
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate , MigrateCommand


 
username = None


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aftermath.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class users(db.Model):
    id = db.Column(db.Integer,primary_key=True, nullable=False)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(256) ,nullable=False)
    email = db.Column(db.String(32), nullable=False)
    firstname = db.Column(db.String(32), nullable=False)
    lastname = db.Column(db.String(32), nullable=False)
   
   
class farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    age_in_days = db.Column(db.Integer, nullable=False)
    age_in_weeks = db.Column(db.String(32), nullable=False)
    timestamp = db.Column(db.DateTime(), nullable=False)
    

class feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    age_in_weeks = db.Column(db.Integer, nullable=False)
    type_of_feed = db.Column(db.String(32), nullable=False)
    intake_per_day = db.Column(db.Integer, nullable=False)

class feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    type_of_feed = db.Column(db.String(64), nullable=False)
    intake_per_day = db.Column(db.String(64), nullable=False)
    age_in_day = db.Column(db.String(64), nullable=False)
    age_in_weeks = db.Column(db.Integer, nullable=False)
    vaccine = db.Column(db.String(64), nullable=False)
    mode_of_vaccine = db.Column(db.String(64), nullable=False)
    temperature = db.Column(db.String(64), nullable=False)

class temperature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    age_in_weeks = db.Column(db.Integer, db.ForeignKey("farm.age_in_weeks"), nullable=False)
    temperature = db.Column(db.String(6))

class vaccines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    age_in_day = db.Column(db.Integer, db.ForeignKey("farm.age_in_days"), nullable=False)
    mode_of_admin = db.Column(db.String(64))
    comments = db.Column(db.String(1000))    

    
   

global username
#For Registration purpose
@app.route ('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        #Ensure not a single field is blank
        data = request.values
        if data['name'] == '' or data['pwd'] == '' or data['pwd2'] == '' or data['email'] == '' or data['firstname'] == '' or data['lastname'] == '':
            return redirect('/register')
        #To ensure the password is the same
        elif data['pwd'] != data['pwd2']:
            
            return redirect ('/register' )
        else :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            flaskdbcur.execute('INSERT INTO users(username, password, email, firstname, lastname) VALUES(%s, %s, %s,%s, %s)',(data['name'],data['pwd'],data['email'],data['firstname'],data['lastname']))
            flaskdb.commit()
            
            return redirect ('/login')

    else:
        return render_template('register.html',title = 'Registration')

# for index route to
@app.route('/')
def index():
    return redirect('/login')
#For the purpose of login methods
@app.route ('/login', methods = ['POST', 'GET'])
def login():
    #We use post http request to check
    if request.method == 'POST':
        data = request.values
        #Ensure the user name and data is not empty
        if data['username'] == ''or data['pwd'] == '' :
            return redirect(url_for('login'))
        #If username and data is there the we check in the db
        else:
            #We pick from the dbc script 

            flaskdb = dbconnect('aftermath','root','')
            #Run the cursor command
            flaskdbcur = flaskdb.cursor()
            #Execute the cursor command to select the db
            flaskdbcur.execute('SELECT * FROM users WHERE username = %s',(data['username'],))
            #Ensure the database is not blank and fetch one
            print ('usernama done')
            if flaskdbcur.rowcount < 0:
                print ('username brought back')
                users = flaskdbcur.fetchone()
                #Once fectched we compare if the value input is same as the databse input
                if users[2] == data['pwd']:
                    global username
                    username = users[1]
                    #if the value is the same it executes this
                    return redirect ('/home/' + users[1])
                #if not it executes this and one is redirected back to his login page
                else:
                    return redirect('/login')
            else:
                return redirect ('login')
    else:
        return render_template('login.html', title = 'Login')


@app.route('/home/<user>', methods = ['POST', 'GET'])
def home(user):

    if request.method == 'POST':
        data = request.values
        if data['no_of_weeks'] <= '1'   :
            print ('user back')
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 1 ")
            data = flaskdbcur.fetchall()
            return render_template( 'homepage.html', data = data) 

        elif data['no_of_weeks'] <= '2' :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            #flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            #flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 2 ORDER BY id DESC")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['no_of_weeks'] <= '3' :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 3 ORDER BY id DESC")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['no_of_weeks'] <= '4' :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 4 ORDER BY id DESC")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['no_of_weeks'] <= '5' :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 5 ORDER BY id DESC")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['no_of_weeks'] <= '6' :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 6 ORDER BY id DESC")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['no_of_weeks'] <= '7' :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))            
            flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 7 ORDER BY id DESC")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['no_of_weeks'] <= '8' :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 8 ORDER BY id DESC")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['no_of_weeks'] <= '9' :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 9 ORDER BY id DESC")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['no_of_weeks'] <= '10' :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 10 ORDER BY id DESC")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 
        else:
           
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            flaskdb.commit()
            return redirect('/home/<user>')

    
    return render_template('homepage.html', title = 'Feeds', user = user ) 


@app.route('/vaccine/<user>', methods = ['POST', 'GET'])
def vaccine(user):
    if request.method == 'POST':
        data = request.values
        if data['no_of_weeks'] <= '1'   :
            print ('user back')
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 1 ")
            data = flaskdbcur.fetchall()
            return render_template( 'homepage.html', data = data) 

        elif data['no_of_weeks'] <= '2' :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            #flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            #flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 2 ORDER BY id DESC")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['no_of_weeks'] <= '3' :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 3 ORDER BY id DESC")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['no_of_weeks'] <= '4' :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 4 ORDER BY id DESC")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['no_of_weeks'] <= '5' :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 5 ORDER BY id DESC")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['no_of_weeks'] <= '6' :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 6 ORDER BY id DESC")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['no_of_weeks'] <= '7' :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))            
            flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 7 ORDER BY id DESC")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['no_of_weeks'] <= '8' :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 8 ORDER BY id DESC")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['no_of_weeks'] <= '9' :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 9 ORDER BY id DESC")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['no_of_weeks'] <= '10' :
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            flaskdb.commit()
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 10 ORDER BY id DESC")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 
        else:
           
            flaskdb = dbconnect('aftermath','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO feed(age_in_weeks,type_of_feed, intake_per_day) VALUES( %s, %s, %s)',(data['no_of_weeks'],data['type_of_feed'],data['intake_per_day'],))
            flaskdb.commit()
            return redirect('/home/<user>')

    return render_template( 'vaccine.html', user = user , title = 'Vaccine') 


@app.route('/temp/<user>', methods = ['POST', 'GET'])
def temp(user):
    return render_template( 'temperature.html', user = user , title = 'Temperature') 

