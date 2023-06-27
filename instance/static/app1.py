from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/new_account')
def new_account():
    return "New Account page"
@app.route('/view_history')
def view_history():
    return "View History page"
if __name__ == '__main__':
    app.run()
