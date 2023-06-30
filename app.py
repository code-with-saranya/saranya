from flask import Flask, render_template, request
import pandas as pd
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.config['MYSQL_HOST'] = 'localhost'  
app.config['MYSQL_USER'] = 'root'   
app.config['MYSQL_PASSWORD'] = 'Welcome2ntt' 
app.config['MYSQL_DB'] = 'global'  

mysql = MySQL(app)



@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.xlsx'):
            
            df = pd.read_excel('C:\\Users\\saranya.govindarajul\\OneDrive - NTT\\Desktop\\pro\\static\\css\\excel\\emply.xlsx')
            name = list(df.name)
            email =list(df.email)

            data = df.to_dict(orient='records')

            cur = mysql.connection.cursor()
            
            query = f"INSERT INTO user(name,email) VALUES ('1','23')"
            cur.execute(query)
                
            mysql.connection.commit()
            cur.close()
            
            return 'File uploaded successfully!'
            
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)


