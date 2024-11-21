import sqlite3
from flask import render_template, url_for, session, request, redirect, Blueprint, flash
from datetime import timedelta

auth = Blueprint('auth', __name__, template_folder='templates')

def init_session_config(app):
    app.permanent_session_lifetime = timedelta(hours=1)
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        try:
            conn = sqlite3.connect('wellnest01.db')
            cursor = conn.cursor()
            cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()
            
            if user and user[0] == password:
                session['user'] = username
                flash('Login successful!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Invalid username or password', 'error')
        except sqlite3.Error as e:
            flash(f'Login error: {str(e)}', 'error')
        finally:
            conn.close()
        
    return render_template('login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = {
            'username': request.form['username'],
            'password': request.form['password'],
            'name': request.form['name'],
            'age': request.form['age'],
            'gender': request.form['gender'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'address': request.form['address'],
            'city': request.form['city'],
            'state': request.form['state'],
            'zip': request.form['zip'],
            'country': request.form['country']
        }
        conn = sqlite3.connect('wellnest01.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (username, password, Name, Age, gender, email, phone, address, city, state, zip, country)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['username'], data['password'], data['name'], data['age'], data['gender'], 
            data['email'], data['phone'], data['address'], data['city'], data['state'], 
            data['zip'], data['country']
        ))
        conn.commit()
        flash('Registration successful! Please login.', 'success')
        conn.close()
        return redirect(url_for('auth.login'))
    return render_template('register.html')


@auth.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.login'))



