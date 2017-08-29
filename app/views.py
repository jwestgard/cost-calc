from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('form.html', 
                            title='Cost Calculator',
                            heading='Digital Preservation Cost Calculator'
                            )
