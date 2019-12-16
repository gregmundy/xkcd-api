FROM python:3.8.0-slim
WORKDIR /xkcd-api

ADD Pipfile Pipfile
ADD Pipfile.lock Pipfile.lock
RUN pip install pipenv && pipenv install --system

ADD xkcd_api xkcd_api