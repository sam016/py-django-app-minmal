#!/bin/bash

# exit on first error
set -e

cecho() {
  local code="\033["
  case "$1" in
    black  | bk) color="${code}0;30m";;
    red    |  r) color="${code}1;31m";;
    green  |  g) color="${code}1;32m";;
    yellow |  y) color="${code}1;33m";;
    blue   |  b) color="${code}1;34m";;
    purple |  p) color="${code}1;35m";;
    cyan   |  c) color="${code}1;36m";;
    gray   | gr) color="${code}0;37m";;
    *) local text="$1"
  esac
  [ -z "$text" ] && local text="$color$2${code}0m"
  echo -e "$text"
}

cecho y "Creating the virualenv..."
virtualenv --python=/usr/bin/python3.6 venv

cecho y "Upgrading pip..."
venv/bin/pip install --upgrade pip

cecho y "Installing the dependecies..."
venv/bin/pip install -r requirements.txt

if [[ "$@" == "--run" ]]
then
    cecho y "Running the server..."
    venv/bin/python manage.py runserver 0.0.0.0:5000
else
    cecho y "Activating the virtualenv..."
    source venv/bin/activate
fi
