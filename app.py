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


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == '' or password == '':
        return render_template('login_errempty.html')  # шаблон если поля пустые
    cursor.execute('SELECT * FROM service.users WHERE login=%s AND password=%s',
                   (str(username), str(password)))
    records = list(cursor.fetchall())
    if len(records) != 0:  # смотрим есть ли данные о пользователе с данным логином и паролем.
        return render_template('account.html', full_name=records[0][1], username=username, password=password)
    else:
        return render_template('login_errlap.html')  # шаблон если пользователь не найден


app.run(debug=True)
