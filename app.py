import requests
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(database='service_db',
                        user='postgres', password='2003', host='127.0.0.1', port='5432')
cursor = conn.cursor()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    cursor.execute('SELECT * FROM service.users WHERE login=%s AND password=%s',
                   (str(username), str(password)))
    records = list(cursor.fetchall())
    return render_template('account.html', full_name=records[0][1])  # test


app.run(debug=True)
