from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

patients = []
seen = []

class Patient:
    def __init__(self, name):
        self.name = name
        self.time = datetime.now()

    def get_details(self):
        return f"{self.name} - {self.time.strftime('%H:%M:%S')}"

@app.route('/')
def home():
    return render_template("home.html", patients=patients, total=len(seen))

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    p = Patient(name)
    patients.append(p)
    return redirect('/')

@app.route('/next')
def next_patient():
    if patients:
        seen.append(patients.pop(0))
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)