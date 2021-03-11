from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql.cursors



app = Flask(__name__)
app.secret_key = 'many random bytes'

"""app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'passer123'
app.config['MYSQL_DATABASE'] = 'gestion_incident'"""



#mysql = MySQL(app)
@app.route('/')
def home():

    data = [["1", "Bon N°1",156,"25/02/21","done"],["2", "Bon N°2",234,"23/02/21","clear"],
              ["3", "Bon N°3",76,"27/02/21","clear"],["4", "bon N°4",1017,"28/02/21","done"],
              ["5", "Bon N°5",1363,"226/02/21","clear"],
            ["6", "Bon N°6", 156, "25/02/21", "done"], ["7", "Bon N°7", 234, "23/02/21", "clear"],
            ["8", "Bon N°8", 76, "27/02/21", "clear"], ["9", "Bon N°9", 1017, "28/02/21", "done"],
            ["10", "Bon N°10", 1363, "226/02/21", "clear"],["11", "Bon N°11", 156, "25/02/21", "done"], ["12", "Bon N°12", 234, "23/02/21", "clear"],
            ["13", "Bon N°13", 76, "27/02/21", "clear"], ["14", "Bon N°14", 1017, "28/02/21", "done"],
            ["15", "Bon N°15", 1363, "226/02/21", "clear"]
            ]
    return render_template('index.html',titre='workflow',tab=data, len=len(data))

@app.route("/test", methods=['POST','GET'])
def test():

    return render_template("test.html")
@app.route("/graphique", methods=['POST','GET'])
def graphique():

    return render_template("index2.html")