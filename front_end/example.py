# -*- coding: utf-8 -*-
import urllib
import time
import re
import os
import datetime
from threading import Thread
import random
import json
import inspect
import urllib
import time

import decimal
import pickle
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey, ForeignKeyConstraint
from flask import Flask, render_template, request, g, session, flash, \
    redirect, url_for, abort, jsonify, make_response
if os.environ.get("heroku"):  # too lazy to get to work on mac
    from flask.ext.cacheify import init_cacheify
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import requests
from flask.ext.script import Manager, Command
from sqlalchemy.sql import text
from flask.ext.mail import Mail, Message
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView
import datetime
import mandrill

try:
    mandrill_api_key = os.environ['MANDRILL_APIKEY']
except:
    mandrill_api_key = 'shit'

mandrill_client = mandrill.Mandrill(mandrill_api_key)


# setup flask
app = Flask(__name__)
manager = Manager(app)
if os.environ.get("heroku"):  # too lazy to get to work on mac
    cache = init_cacheify(app)


SECRET_KEY = 'sldfjsf'

DEBUG_var = True

app.config.update(
    DATABASE_URI=DBURI,
    SECRET_KEY=SECRET_KEY,
    DEBUG=DEBUG_var
)

# setup sqlalchemy
engine = create_engine(app.config['DATABASE_URI'])
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))



#jinja
app.jinja_env.add_extension('jinja2.ext.loopcontrols')



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/annotation_endpoint/annotations', methods=['GET', 'POST'])
def annotation_endpoint():
    print request.form
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


if __name__ == '__main__':
    manager.run()
