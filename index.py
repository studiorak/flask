#!../venv/bin/python

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def mod_index():
  return render_template('mod_index/index.html')

@app.route('/hello/<username>')
def mod_hello(username):
  return render_template('mod_hello/index.html',name=username)
