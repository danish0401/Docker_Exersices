# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker


COPY . .

RUN python -m pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt
CMD [ "python", "app.py"]