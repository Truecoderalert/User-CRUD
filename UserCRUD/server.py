from flask import Flask, request, render_template, redirect, session
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('User_form.html')

@app.route('/user/new' , methods=['post'])
def turntoresult():
    data = {'first_name':request.form['first_name'], 'last_name':request.form['last_name'], 'email':request.form['email'] }
    User.create(data)
    return redirect('/user/show')

@app.route('/user/show')
def showresult():
    users = User.get_all()
    return render_template ('showresult.html' ,  users = users)

    


if __name__=='__main__':
    app.run(debug=True)