#!./venv/bin/python

from flask import Flask, render_template
from mod_hello import *

app = Flask(__name__)

import mod_hello
