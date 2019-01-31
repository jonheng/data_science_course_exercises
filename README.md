# Data Science Bootcamp

### Setup

1. Clone repository: `https://github.com/jonheng/data_science_course_exercises`
2. Set up local environment: `./setup.sh`

Steps for working with jupyter notebook
- Build image: `docker build -t twsg-data/data-science-bootcamp-notebooks -f Dockerfile.jupyter .`
- Start container: `docker run -it -p 8888:8888 -v $(pwd):/var/code --name notebooks twsg-data/data-science-bootcamp-notebooks`
- Visit `http://localhost:8888/?token=<copy token from terminal>`
- To stop jupyter notebook, hit Ctrl+C

Steps for running flask app
- `docker build -t twsg-data/data-science-bootcamp-webapp -f Dockerfile.webapp .`
- `docker run -it -p 8080:8080 -v $(pwd):/var/code --name model-web-app twsg-data/data-science-bootcamp-webapp`