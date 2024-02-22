from flask import Flask, request, redirect, render_template, send_from_directory, url_for
import os
from werkzeug.utils import secure_filename

BASE_DIR = os.getcwd()
