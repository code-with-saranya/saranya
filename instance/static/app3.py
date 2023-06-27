from flask import Flask, render_template, request
app = Flask(__name__)
history = []
@app.route('/')
def home():
    return render_template('index.html', history=history)
@app.route('/add', methods=['POST'])
def add_record():
    record = request.form['record']
    history.append(record)
    return render_template('index.html', history=history)
@app.route('/delete', methods=['POST'])
def delete_record():
    record = request.form['record']
    if record in history:
        history.remove(record)
    return render_template('index.html', history=history)
if __name__ == '__main__':
    app.run()
