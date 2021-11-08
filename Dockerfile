#Deriving the latest base image
FROM python:latest
LABEL Maintainer="patrikfejda"
WORKDIR /usr/app/src
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY graf.py ./
