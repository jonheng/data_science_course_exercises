# Data Science Bootcamp

### Setup

1. Clone repository: `https://github.com/jonheng/data_science_course_exercises`
2. Set up local environment: `./setup.sh`

Steps for working with jupyter notebook
- Start notebook: `docker run -v $(pwd):/home/jovyan/work -p 8888:8888 --name scipy-notebook jupyter/scipy-notebook`
- Visit `http://localhost:8888/?token=<copy token from terminal>`
- To stop jupyter notebook, hit Ctrl+C

Steps for running flask app
- `docker build -t twsg-data/data-science-bootcamp .`
- `docker run -it -p 8080:8080 -v $(pwd):/var/code --name model-web-app twsg-data/data-science-bootcamp`