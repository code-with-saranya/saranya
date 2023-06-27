from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def student_details():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        return render_template('success.html', name=name)
    return render_template('form.html')
if __name__ == '__main__':
    app.run(debug=True)
