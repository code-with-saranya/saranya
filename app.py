from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import pandas as pd
import sqlite3

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
app.app_context().push()
app.config["UPLOAD_FOLDER"]="static/excel"

class Todo(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200), nullable=False)
    address=db.Column(db.String(500), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}"


@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
       name=request.form['name']
       address=request.form['address']
       todo=Todo(name=name, address=address)
       db.session.add(todo)
       db.session.commit()
    allTodo=Todo.query.all()
    return render_template('index.html', allTodo=allTodo)
   


@app.route('/show')
def products():
    allTodo=Todo.query.all()
    print(allTodo)
    return 'this is products page'
    
@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
       name=request.form['name']
       address=request.form['address']
       todo=Todo.query.filter_by(sno=sno).first()
       todo.name=name
       todo.address=address
       db.session.add(todo)
       db.session.commit()
       return redirect("/")
    todo=Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo=Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")



@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method=="POST":
        upload_excel=request.files['upload_excel']
        if upload_excel.filename !='':
            filepath=os.path.join(app.config["UPLOAD_FOLDER"],upload_excel.filename)
            upload_excel.save(filepath)
            data_frame = pd.read_excel('C:\\Users\\saranya.govindarajul\\OneDrive - NTT\\Desktop\\task3\\static\\css\\excel\\data1.xlsx')
            connection = sqlite3.connect('C:\\Users\\saranya.govindarajul\\OneDrive - NTT\\Desktop\\task3\\instance\\todo.db')
            cursor = connection.cursor() 
            cursor.execute('SELECT * FROM todo')
            rows = cursor.fetchall()
            for index, row in data_frame.iterrows():
                Name= row['Name']
                Address = row['Address']
               
                insert_query = f"INSERT INTO todo (Name, Address) VALUES (?, ?)"
                cursor.execute(insert_query, (Name, Address))
            connection.commit()
            connection.close()
        return render_template('index.html') 
       
    return render_template('upload.html')  
if __name__ =="__main__":
    app.run(debug=True, port=8000)