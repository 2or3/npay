FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /code

COPY ./app/Pipfile /code/
COPY ./app/Pipfile.lock /code/
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN /usr/local/bin/python -m pip install pipenv
RUN pipenv install
