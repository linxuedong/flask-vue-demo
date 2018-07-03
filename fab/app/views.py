from flask import render_template, jsonify
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, BaseView, expose
from app import appbuilder, db
from random import randint

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404


db.create_all()


class Api(BaseView):
    default_view = "random"

    @expose('/random')
    def random(self):
        response = {
            'randomNumber': randint(1, 100)
        }
        return jsonify(response)


class RandomView(BaseView):
    route_base = '/'
    default_view = 'random'

    @expose('random')
    def random(self):
        return self.render_template('random.html')


appbuilder.add_view_no_menu(Api)
appbuilder.add_view(RandomView, 'random', category="Random")
