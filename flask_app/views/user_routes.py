from flask import Blueprint, request, url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from flask_app.models.user_models import User
from flask_app import db

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/')
def user():
    user_list = []
    users = db.session.query(User).all()
    for user in users:
        user_list.append({"id":user.id, "username":user.username, "age":user.age, "sex":user.sex, "bmi":user.bmi, "smoker":user.smoker})
    
    return render_template('user.html', user_list=user_list)

@bp.route('/add')
def add():
    return render_template('add_user.html')

@bp.route('/api/create', methods=['POST'])
def create():
    username = request.form.get('username')
    age = request.form.get('age')
    sex = request.form.get('sex')
    bmi = request.form.get('bmi')
    smoker = request.form.get('smoker')

    user = User(username=username, age=age, sex=sex, bmi=bmi, smoker=smoker)

    db.session.add(user)
    db.session.commit()

    return render_template('read_user.html', user=user)

@bp.route('/api/read', methods=['POST'])
def read():
    username = request.form.get('username')
    user = db.session.query(User).filter_by(username=username).first()

    return render_template('read_user.html', user=user)

@bp.route('/modify/<username>')
def modify(username):
    return render_template('modify_user.html', username=username)

@bp.route('/api/update', methods=['POST'])
def update():
    username = request.form.get('username')
    user = db.session.query(User).filter_by(username=username).first()

    age = request.form.get('age')
    sex = request.form.get('sex')
    bmi = request.form.get('bmi')
    smoker = request.form.get('smoker')

    user.age = age
    user.sex = sex
    user.bmi = bmi
    user.smoker = smoker
    
    db.session.commit()

    return redirect(url_for('user.user'))

@bp.route('/api/delete/<username>')
def delete(username):
    user = db.session.query(User).filter_by(username=username).first()

    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('user.user'))