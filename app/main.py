#!/usr/bin/env python
# -.- coding: utf-8 -.-


import os
from docutils.core import publish_parts

from flask import Flask, render_template, request

app = Flask(__name__)

app.config.from_object('config.DevelConfig')


@app.route('/')
def card():
    
    src_dir = app.config['SRC_DIR']

    card_holder = []
    for i in os.listdir(src_dir):
        if i not in app.config['EXCLUDE_DIR_LIST'] and os.path.isdir(os.path.join(src_dir, i)):
            card_holder.append(i)

    cards = []
    nav = request.args.get('nav', '')
    if nav:
        for i in os.listdir(os.path.join(src_dir, nav)):
            fn, ext = os.path.splitext(i)
            if ext == '.txt':
                cards.append(fn)

    body = ''
    card = request.args.get('card', '')
    if nav and card:
        content = open(os.path.join(src_dir, nav, '%s.txt'%card)).read().decode('u8')
        body = publish_parts(content, writer_name='html')['html_body']
        
    return render_template('index.html',
                           card_holder=card_holder,
                           cards=cards,
                           body=body)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7821)
