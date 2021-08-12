from flask import Blueprint, render_template, request, url_for
from flask_app import db
from flask_app.models.user_models import User
from werkzeug.utils import redirect
from flask_app.utils.main_funcs import predict_premium

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/predict', methods=["GET"])
def predict():
    user_list = []
    users = db.session.query(User).all()
    for user in users:
        user_list.append({"id":user.id, "username":user.username, "age":user.age, "sex":user.sex, "bmi":user.bmi, "smoker":user.smoker})

    return render_template('predict.html', user_list=user_list)

@bp.route('/predict/form/new', methods=["POST"])
def predict_new():
    age = request.form.get('age')
    sex = request.form.get('sex')
    bmi = request.form.get('bmi')
    smoker = request.form.get('smoker')

    result = round(predict_premium(int(age), sex, float(bmi), smoker), 2)
    result_losebmi = round(predict_premium(int(age), sex, float(bmi)-1, smoker), 2)
    result_nonsmoker = round(predict_premium(int(age), sex, float(bmi), "no"), 2)
    result_both = round(predict_premium(int(age), sex, float(bmi)-1, "no"), 2)
    return render_template('result.html', result=result, result_losebmi=result_losebmi, result_nonsmoker=result_nonsmoker, result_both=result_both)

@bp.route('/predict/<username>')
def predict_user(username):
    user = db.session.query(User).filter_by(username=username).first()
    result = round(predict_premium(user.age, user.sex, user.bmi, user.smoker), 2)
    result_losebmi = round(predict_premium(user.age, user.sex, user.bmi-1, user.smoker), 2)
    result_nonsmoker = round(predict_premium(user.age, user.sex, user.bmi, "no"), 2)
    result_both = round(predict_premium(user.age, user.sex, user.bmi-1, "no"), 2)

    return render_template('result.html', result=result, result_losebmi=result_losebmi, result_nonsmoker=result_nonsmoker, result_both=result_both)