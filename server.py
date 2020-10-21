from flask import Flask, render_template, session, request,redirect

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route('/')
def show_homepage():
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    return render_template("form.html")

@app.route('/results')
def show_results():
    adj = request.args.getlist('quality')
    name = session['name']
    return render_template("results.html",result=adj,person=name)

@app.route("/save-name")
def save_name():
    username = request.args.get('name')
    session['name'] = username 
    return redirect("/form")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
