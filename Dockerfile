FROM python:3.12
COPY requirements.txt /Websiteproject/
WORKDIR /Websiteproject
RUN pip install -r requirements.txt 
COPY . /Websiteproject
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]