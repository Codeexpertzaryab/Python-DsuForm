from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
local_server = True
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:zaryab@localhost/Form"
db=SQLAlchemy(app)

class form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50),nullable=False)
    lname = db.Column(db.String(50),nullable=False)
    birthday = db.Column(db.String(10),nullable=False)
    gender=db.Column(db.String(10),nullable=False)
    email=db.Column(db.String(50), nullable=False)
    phone=db.Column(db.String(12), nullable=False)
    subjects=db.Column(db.String(50),nullable=False)


@app.route("/",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        birthday=request.form.get('birthday')
        gender=request.form['g']
        email=request.form.get('email')
        phone=request.form.get('phone')
        subjects=request.form.get('subject')
        entry = form(fname=fname,lname=lname,birthday=birthday,gender=gender,email=email,phone=phone,subjects=subjects)
        db.session.add(entry)
        db.session.commit()
    return render_template('index.html'),404

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)