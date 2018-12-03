from flask import Flask, render_template,jsonify
import pyodbc

app = Flask(__name__, template_folder='Templates')

emps = [
    {'id': '101', 'name': 'Aravind'},
    {'id': '102', 'name': 'Ravi'},
    {'id': '103', 'name': 'Raju'},
    {'id': '104', 'name': 'Ramesh'},
    {'id': '105', 'name': 'Shiva'},
]


@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', title='Home Page', emps=emps)

@app.route('/jsons')
def jsonsemps():
    return render_template('jsonsemps.html', title='employees', emps = jsonify(emps))

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Page not found on this website</h1>",404

@app.route('/emps')
def employees():
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=trngsql.ajrgroup.in;'
        'DATABASE=Aravind;'
        'UID=sa;'
        'PWD=Welcome@123'
    )

    cursor = conn.cursor()
    cursor.execute("select * from customerdata")
    result = cursor.fetchall()
    return render_template('emps.html', title='Employees', result=result)


@app.route('/about')
def about():
    return render_template('about.html', title="About Page")


if __name__ == '__main__':
    app.run(debug=True)
