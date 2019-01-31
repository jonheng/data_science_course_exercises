FROM jupyter/scipy-notebook

ENV FLASK_APP=app
ENV FLASK_DEBUG=1

WORKDIR /var/code
ADD requirements.txt /var/code

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "flask" ]

CMD [ "app/web_server.py" ]