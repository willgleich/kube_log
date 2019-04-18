from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
import kube_log

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


class LogForm(FlaskForm):
    choice = kube_log.get_pods_for_selectfield('metallb-system')
    pod = SelectField('Kubernetes pod', choices=choice)
    lines = TextField()
    submit = SubmitField()


@app.route('/', methods=['GET', 'POST'])
def kube_log_view():
    form = LogForm()
    if form.validate_on_submit():
        return render_template('kube_log.html', form=form, data=kube_log.get_pod_logs(form.data['pod'], 'metallb-system'))
    return render_template('kube_log.html', form=form)


if __name__ == '__main__':
    app.run()
