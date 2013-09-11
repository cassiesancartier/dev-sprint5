import flask, flask.views
import os
import utils


class Budget(flask.views.MethodView):
    @utils.login_required
    def get(self):
        return flask.render_template('budget.html')

    #@utils.login_required
    #def post(self):
    #    result = eval(flask.request.form['expression'])
    #    flask.flash(result)
    #    return flask.redirect(flask.url_for('remote'))