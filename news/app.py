#!/usr/bin/env python3

from flask import Flask
from flask import render_template, abort
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    filelist = os.listdir('/home/shiyanlou/files')
    new_file = []
    for file in filelist:        
        with open(os.path.join('/home/shiyanlou/files',file),'r') as f:
            file_dict = json.loads(f.read())
            new_file.append(file_dict['title'])
    return render_template('base.html',filetitle = new_file)
    
@app.route('/files/<filename>')
def file(filename):
    filequancheng = filename + '.json'
    absfilepath = os.path.join('/home/shiyanlou/files',filequancheng)
    if not os.path.exists(absfilepath):
        abort(404)
    with open(absfilepath,'r') as f:
        file_dict = json.loads(f.read())
    return render_template('file.html',file=file_dict)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

    
    
if __name__ == '__main__':
    app.run()
