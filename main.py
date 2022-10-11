from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/home")
def home():
   return render_template("index.html")

@app.route("/about")
def about():
   return render_template("about.html")

@app.route("/contact")
def contact():
   return render_template("contact.html")

@app.route("/friends")
def friends():
   return render_template("friends.html")

@app.route("/success/<name>")
def success(name):
    return "Welcome %s" % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))

if __name__ == "__main__":
   app.run()