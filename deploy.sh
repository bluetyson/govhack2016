#!/bin/bash
# RUN ME IN THE PROJECT ROOT!!

pip install -r requirements.txt

git pull origin master
git checkout master

pkill gunicorn
gunicorn -w 4 govhack2016:app -b 127.0.0.1:5000 &