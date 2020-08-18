from flask import Flask,render_template,request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

db = yaml.load(open("db.yaml"))
app.config['MYSQL_HOST'] = db["mysql_host"]
app.config['MYSQL_USER'] = db["mysql_user"]
app.config['MYSQL_PASSWORD'] = db["mysql_password"]
app.config['MYSQL_DB'] = db["mysql_db"]

mysql = MySQL(app)

@app.route('/login',methods=["GET","POST"])
def login():
   if request.method=="POST":
      userDetails = request.form
      name = userDetail["name"]
      email = userDetails["email"]
      cur = mysql.connection.cursor()
      cur.execute("INSERT INTO users(name,email) VALUES(%s,%s)",(name,email))
      mysql.connection.commit()
      cur.close()
      return"success"
   return render_template("login.html")

@app.route('/profile')
def profile():
   return render_template("profile.html")
   
#@app.route('/login',method=[POST])
#def Authenticate():
 #  username = request.form['u']
  # password = request.form['p']
   #cursor = mysql.connect().cursor()
   #cursor.execute("SELECT * from User where username='" + username + "'and password='" + password +"'")
   #data = cursor.fetchone()
   #if data is None:
    #  return "Username or Password is wrong"
     # else:
      #   return "login sucessful"

@app.route('/register')
def register():
   return render_template("register.html")
   
   


if __name__=="__main__":
    app.run(debug=True)