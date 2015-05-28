#!/usr/bin/env python
# -.- coding: utf-8 -.-


import os
from flask import Flask, render_template, redirect, request, url_for, abort, current_app


app = Flask(__name__)

app.config.from_object('config.DevelConfig')


@app.route('/')
def notebook():
    nblist = []
    notebook_path = current_app.config['NOTEBOOK_PATH']

    nb = request.args.get('n', '')
    tab = request.args.get('t', '')
    page = request.args.get('p', '')

    for root, dirs, files in os.walk(notebook_path):
        if root == notebook_path:
            nblist = dirs
    notebook = nb or nblist[0]
    
    tab_path = os.path.join(notebook_path, notebook)
    tablist = None
    for root, dirs, files in os.walk(tab_path):
        if root == tab_path:
            tablist = dirs
    tab = tab or tablist[0]
    
    page_path = os.path.join(tab_path, tab)
    pagelist = None
    for root, dirs, files in os.walk(page_path):
        if root == page_path:
            pagelist = files
            
    page = page or pagelist[0]

    content = open(os.path.join(page_path, page)).read().decode('u8')
    
    return render_template('notebook.html',
                           notebook=notebook,
                           notebooks=nblist,
                           tab=tab,
                           tablist=tablist,
                           page=page,
                           pagelist=pagelist,
                           content=content)


if __name__ == '__main__':
    app.run()
