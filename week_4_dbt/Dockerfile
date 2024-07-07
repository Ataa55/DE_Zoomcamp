FROM python:3.9

RUN apt-get update && apt-get install -y git && apt-get install nano
RUN git clone https://github.com/dbt-labs/dbt.git /usr/local/dbt

WORKDIR /usr/local/dbt
RUN pip install -r requirements.txt

RUN git clone https://github.com/dbt-labs/dbt-postgres.git && \
    cd dbt-postgres && \
    python -m pip install .
