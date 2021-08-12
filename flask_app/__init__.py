# __init__.py
# Flask 어플리케이션을 실행하기 위한 초기 app 제공

import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from flask_app.views import user_routes
    from flask_app.views import main_routes
    app.register_blueprint(user_routes.bp)
    app.register_blueprint(main_routes.bp)

    @app.route('/', methods=['POST', 'GET'])
    def index():
        apple = 'red'
        apple_count = 10
        return render_template('index_old.html', fruit_color=apple, number=apple_count, var=[1, 2, 3], fruits={'apple':'red', 'banana':'yellow'}, vegetables=['cucumber', 'spinach'], item_list=['book', 'keyboard', 'window'])

    @app.route('/index/', defaults={ 'num' : 0 })
    @app.route('/index/<num>')
    def index_number(num):
        return 'Wlecome to Index %i' % int(num)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()