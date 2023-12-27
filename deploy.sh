#!/bin/bash
echo "Blank Slate Deployment --- `date +%m`/`date +%d`/`date +%Y` `date +%r`"

# Django Migrate
python3 ./blankslate/manage.py makemigrations words
python3 ./blankslate/manage.py migrate

# Git Update
git status
git pull 
git add . 
git commit -m "Deploy --- `date +%m`/`date +%d`/`date +%Y` `date +%r`"
git push