from flask import Flask,request
from flask import render_template,redirect,url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object('config')

# connect to another MongoDB database on the same host
mongo = PyMongo(app, config_prefix='MONGO')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/aa')
def aa():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("index.html",
        title = 'Home',
        user = user)


@app.route('/chart',methods=("GET", "POST"))
def chart(ps=80):
    ps=ps
    return render_template("chart.html",**locals())


@app.route('/tm')
def tm():
    data = mongo.db.project.find_one_or_404()
    return render_template("tm.html",**locals())

@app.route("/im")
def im():
    data = {'id':'111','project':'msub1111'}
    mongo.db.project.insert_one(data)
    return 'ok'

@app.route("/login",methods=("GET", "POST"))
def login():
    error = None
    if request.method == 'POST':
        if request.form['username']=='admin':
            return redirect(url_for('home',username=request.form['username']))
        else:
            error = 'Invalid username/password'
    return  render_template("login.html")

@app.route('/adata',methods=("GET", "POST"))
def adata():
    data = request.json
    if data is None:
        return "param error"
    try:
        ret = mongo.db.project.insert_one(data)
    except:
        return "mongo err"
    finally:
        return '1'

@app.route("/gets",methods=("GET", "POST"))
def gets():
    data = request.json
    print data
    data1 = {'id':'111','project':'msub'}
    print type(data1)
    #mongo.db.project.insert_one(data)
    return data.__str__()

if __name__ == '__main__':
    app.run("0.0.0.0",'80')
