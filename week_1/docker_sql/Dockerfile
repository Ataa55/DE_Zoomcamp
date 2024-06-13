FROM python:3.9

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
COPY IngestToPostgres.py IngestToPostgres.py

ENTRYPOINT [ "python", "IngestToPostgres.py" ]