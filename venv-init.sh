#!/bin/bash

# exit on first error
set -e

# colored echo
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

# checks if the argument exists
has_arg() {
  first="$1"
  shift
  if [[ "$@" == *"$first"* ]]
  then
      echo 1
  fi
}

skip_venv=$(has_arg "--skip-venv" "$@")
djg_run=$(has_arg "--run" "$@")

if [[ $skip_venv ]]
then
  cecho y "Skipping creating the virualenv..."
else
  cecho c "Creating the virualenv..."
  virtualenv --python=/usr/local/bin/python3.7 venv
fi

cecho c "Upgrading pip..."
venv/bin/pip install --upgrade pip

cecho c "Installing the dependecies..."
venv/bin/pip install -r requirements.txt

if [[ $djg_run ]]
then
    cecho c "Running migration ..."
    venv/bin/python manage.py migrate

    cecho c "Running the server..."
    venv/bin/python manage.py runserver 0.0.0.0:5000
else
    cecho c "Activating the virtualenv..."
    source venv/bin/activate
fi
