FROM python:3.12
WORKDIR /WEBSITEPROJECT
COPY . /WEBSITEPROJECT
CMD http://127.0.0.1:8000/