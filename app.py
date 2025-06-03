from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Person, User
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///acreditacion.db'
app.config['SECRET_KEY'] = 'change_me'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', password=generate_password_hash('admin'))
        db.session.add(admin)
        db.session.commit()

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    persons = Person.query.filter(Person.accredited_at.isnot(None)).all()
    total = len(persons)
    return render_template('index.html', persons=persons, total=total)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('index'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/accredit/<int:person_id>')
def accredit(person_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    person = Person.query.get_or_404(person_id)
    person.accredited_at = datetime.utcnow()
    person.accredited_by = session.get('username')
    db.session.commit()
    if person.special:
        flash(f"Llegó una persona especial: {person.name} - {person.special_reason}")
    return redirect(url_for('index'))

@app.route('/manual', methods=['GET', 'POST'])
def manual():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        cargo = request.form['cargo']
        company = request.form['company']
        special = 'special' in request.form
        reason = request.form.get('reason')
        person = Person(name=name, cargo=cargo, company=company,
                        special=special, special_reason=reason)
        db.session.add(person)
        db.session.commit()
        flash('Persona agregada exitosamente')
        return redirect(url_for('manual'))
    return render_template('manual.html')

if __name__ == '__main__':
    app.run(debug=True)
