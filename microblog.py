#-*- coding:utf-8 -*-
'''
author：baizhou
'''

from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}



app.run(debug=True,
        host='0.0.0.0',
        port='8000')
