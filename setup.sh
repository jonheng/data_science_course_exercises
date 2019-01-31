#!/usr/bin/env bash

which brew
if [ $? -ne 0 ]; then
  echo "INFO: Installing homebrew"
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi

echo "INFO: Installing docker if not installed"
command -v docker >/dev/null 2>&1 || brew cask install docker 

open --background -a Docker
while ! docker system info > /dev/null 2>&1; do sleep 1 && echo "[INFO] Waiting for docker daemon startup to complete..."; done

docker pull jupyter/scipy-notebook
docker run -v $(pwd):/home/jovyan/work -p 8888:8888 jupyter/scipy-notebook

echo "================ 🚀 🚀 🚀 🚀 🚀 🚀 ================ "
echo "Setup completed."
echo "To start jupyter notebook, run: docker run -v $(pwd):/home/jovyan/work -p 8888:8888 jupyter/scipy-notebook"
echo "To stop jupyter notebook, hit Ctrl+C"