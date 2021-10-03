from flask import Flask, render_template, url_for
from datetime import datetime

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/works')
def works():
    return render_template('works.html')



if __name__=="__main__":
    app.run(debug=True)