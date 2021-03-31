FROM python:latest

ADD LargeFile.py  .

RUN pip install pandas mysql.connector

CMD [ "python","./LargeFile.py" ]