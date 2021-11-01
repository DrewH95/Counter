from flask import Flask, render_template, session, redirect
app = Flask (__name__)
app.secret_key = 'pumpkin'

@app.route ('/') 
def index():
    if 'visit' in session:
        session['visit'] += 1
    else:
        session['visit'] = 1
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0

    return render_template("index.html")


@app.route('/clear')
def clear():
    session.clear() 
    return redirect('/')
    # be sure to redirect back to home page
# this route will clear the current session and start back at 0




if __name__== "__main__":
    app.run (debug=True) 