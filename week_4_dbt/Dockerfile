#my base image
FROM python:3.9

#update the system and install nano  editor
RUN apt-get update && apt-get install -y git && apt-get install nano
#clone dbt repo to 
RUN git clone https://github.com/dbt-labs/dbt.git /usr/local/dbt

#open new shell at this path
WORKDIR /usr/local/dbt 
#install the requirments
RUN pip install -r requirements.txt
#clone postgres adabter repo and start installing
RUN git clone https://github.com/dbt-labs/dbt-postgres.git && \
    cd dbt-postgres && \
    python -m pip install .
