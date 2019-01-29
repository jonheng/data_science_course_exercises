#!/usr/bin/env bash

which brew
if [ $? -ne 0 ]; then
  echo "INFO: Installing homebrew"
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi

which python3
if [ $? -ne 0 ]; then
  echo "INFO: Installing python3"
  brew install python3
fi

virtual_environment_name=".$(basename $(pwd))"
python3 -m venv $virtual_environment_name

source $virtual_environment_name/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

python -m ipykernel install --user --name=${virtual_environment_name}

echo "================ 🚀 🚀 🚀 🚀 🚀 🚀 ================ "
echo "Setup completed."
echo "To get started, run the following commands:"
echo "- source $virtual_environment_name/bin/activate"
echo "- jupyter notebook"
echo "To stop jupyter notebook, hit Ctrl+C"