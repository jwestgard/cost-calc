from flask import render_template, request
from app import app
from flask_bootstrap import Bootstrap
from .forms import SubmissionForm

app.config['SECRET_KEY'] = 'f00b@rb@z sp@m@l0t'
bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', 
                            title='Cost Calculator',
                            heading='Digital Preservation Cost Calculator'
                            )

@app.route('/form', methods = ['GET', 'POST'])
def submission():
    form = SubmissionForm()
    return render_template('form.html', form=form)
