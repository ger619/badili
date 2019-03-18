from flask import Flask, render_template , url_for, request , redirect , flash
from dbc import dbconnect

 
username = None


app = Flask(__name__)

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
            flaskdb = dbconnect('projectbadili','root','')
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

            flaskdb = dbconnect('projectbadili','root','')
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
    #This is used to call the database and authenticate select all and display
#    flaskdb = dbconnect('projectbadili','root','')
 #   flaskdbcur = flaskdb.cursor()
  #  flaskdbcur.execute("SELECT * FROM feedback Where id = 1 ORDER BY id DESC")
   # data = flaskdbcur.fetchall()

    if request.method == 'POST':
        data = request.values
        if data['age_in_day'] >= '1'   :
            flaskdb = dbconnect('projectbadili','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO chicken(name_of_farmer, age_in_day, no_of_weeks, type_of_feed, type_of_vaccines, comments) VALUES(%s, %s, %s, %s, %s, %s)',( username, data['age_in_day'],data['no_of_weeks'],data['type_of_feed'],data['type_of_vaccines'],data['comments'],))
            flaskdb.commit()
            print('Db Execute')
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 1 ORDER BY id DESC")
            print ("search execute")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['age_in_day'] >= '2' and data['no_of_weeks'] != ''  :
            flaskdb = dbconnect('projectbadili','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO chicken(name_of_farmer, age_in_day, no_of_weeks, type_of_feed, type_of_vaccines, comments) VALUES(%s, %s, %s, %s, %s, %s)',( username, data['age_in_day'],data['no_of_weeks'],data['type_of_feed'],data['type_of_vaccines'],data['comments'],))
            flaskdb.commit()
            print('Db Execute')
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 2 ORDER BY id DESC")
            print ("search execute")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['age_in_day'] >= '3' :
            flaskdb = dbconnect('projectbadili','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO chicken(name_of_farmer, age_in_day, no_of_weeks, type_of_feed, type_of_vaccines, comments) VALUES(%s, %s, %s, %s, %s, %s)',( username, data['age_in_day'],data['no_of_weeks'],data['type_of_feed'],data['type_of_vaccines'],data['comments'],))
            flaskdb.commit()
            print('Db Execute')
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 3 ORDER BY id DESC")
            print ("search execute")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['age_in_day'] >= '4' :
            flaskdb = dbconnect('projectbadili','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO chicken(name_of_farmer, age_in_day, no_of_weeks, type_of_feed, type_of_vaccines, comments) VALUES(%s, %s, %s, %s, %s, %s)',( username, data['age_in_day'],data['no_of_weeks'],data['type_of_feed'],data['type_of_vaccines'],data['comments'],))
            flaskdb.commit()
            print('Db Execute')
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 4 ORDER BY id DESC")
            print ("search execute")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['age_in_day'] >= '5' :
            flaskdb = dbconnect('projectbadili','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO chicken(name_of_farmer, age_in_day, no_of_weeks, type_of_feed, type_of_vaccines, comments) VALUES(%s, %s, %s, %s, %s, %s)',( username, data['age_in_day'],data['no_of_weeks'],data['type_of_feed'],data['type_of_vaccines'],data['comments'],))
            flaskdb.commit()
            print('Db Execute')
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 5 ORDER BY id DESC")
            print ("search execute")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['age_in_day'] >= '6' :
            flaskdb = dbconnect('projectbadili','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO chicken(name_of_farmer, age_in_day, no_of_weeks, type_of_feed, type_of_vaccines, comments) VALUES(%s, %s, %s, %s, %s, %s)',( username, data['age_in_day'],data['no_of_weeks'],data['type_of_feed'],data['type_of_vaccines'],data['comments'],))
            flaskdb.commit()
            print('Db Execute')
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 6 ORDER BY id DESC")
            print ("search execute")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['age_in_day'] >= '7' :
            flaskdb = dbconnect('projectbadili','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO chicken(name_of_farmer, age_in_day, no_of_weeks, type_of_feed, type_of_vaccines, comments) VALUES(%s, %s, %s, %s, %s, %s)',( username, data['age_in_day'],data['no_of_weeks'],data['type_of_feed'],data['type_of_vaccines'],data['comments'],))
            flaskdb.commit()
            print('Db Execute')
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 7 ORDER BY id DESC")
            print ("search execute")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['age_in_day'] >= '8' :
            flaskdb = dbconnect('projectbadili','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO chicken(name_of_farmer, age_in_day, no_of_weeks, type_of_feed, type_of_vaccines, comments) VALUES(%s, %s, %s, %s, %s, %s)',( username, data['age_in_day'],data['no_of_weeks'],data['type_of_feed'],data['type_of_vaccines'],data['comments'],))
            flaskdb.commit()
            print('Db Execute')
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 8 ORDER BY id DESC")
            print ("search execute")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['age_in_day'] >= '9' :
            flaskdb = dbconnect('projectbadili','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO chicken(name_of_farmer, age_in_day, no_of_weeks, type_of_feed, type_of_vaccines, comments) VALUES(%s, %s, %s, %s, %s, %s)',( username, data['age_in_day'],data['no_of_weeks'],data['type_of_feed'],data['type_of_vaccines'],data['comments'],))
            flaskdb.commit()
            print('Db Execute')
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 9 ORDER BY id DESC")
            print ("search execute")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 

        elif data['age_in_day'] >= '10' :
            flaskdb = dbconnect('projectbadili','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO chicken(name_of_farmer, age_in_day, no_of_weeks, type_of_feed, type_of_vaccines, comments) VALUES(%s, %s, %s, %s, %s, %s)',( username, data['age_in_day'],data['no_of_weeks'],data['type_of_feed'],data['type_of_vaccines'],data['comments'],))
            flaskdb.commit()
            print('Db Execute')
            flaskdbcur.execute("SELECT * FROM feedback WHERE id = 10 ORDER BY id DESC")
            print ("search execute")
            data = flaskdbcur.fetchall()            
            return render_template( 'homepage.html', data = data) 
        else:
           
            flaskdb = dbconnect('projectbadili','root','')
            flaskdbcur = flaskdb.cursor()
            global username
            flaskdbcur.execute('INSERT INTO chicken(name_of_farmer, age_in_day, no_of_weeks, type_of_feed, type_of_vaccines, comments) VALUES(%s, %s, %s, %s, %s, %s)',( username, data['age_in_day'],data['no_of_weeks'],data['type_of_feed'],data['type_of_vaccines'],data['comments'],))
            flaskdb.commit()
            return redirect('/home/<user>')

#   if data['age_in_day'] == '' or data['no_of_weeks'] =="" or data['type_of_feed'] =="" or data['type_of_vaccines'] =="":
#       data = request.values
#       flaskdb = dbconnect('projectbadili','root','')
#       flaskdbcur = flaskdb.cursor()
#       flaskdbcur.execute("SELECT * FROM chicken ORDER BY id DESC")
#       data = flaskdbcur.fetchall()
#       return redirect('/home/<user>')
    
#    elif data['age_in_day'] == '' or data['no_of_weeks'] =="" or data['type_of_feed'] =="" or data['type_of_vaccines'] =="":
#        flaskdb = dbconnect('projectbadili','root','')
#        flaskdbcur = flaskdb.cursor()
#        flaskdbcur.execute("SELECT * FROM chicken ORDER BY id DESC")
#        data = flaskdbcur.fetchall()
#    else :
#        flaskdb = dbconnect('projectbadili','root','')
#        flaskdbcur = flaskdb.cursor()
#        flaskdbcur.execute("SELECT * FROM chicken ORDER BY id DESC")
#        data = flaskdbcur.fetchall()


    
    return render_template('homepage.html', title = 'Profile', user = user )

