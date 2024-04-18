FROM python:3.12-slim
WORKDIR /BGEvr

#COPY ./BGEvr/run_bot.py /BGEvr/run_bot.py
RUN apt-get update
#RUN apt-get install -y python3-dev libpq-dev
COPY ./BGEvr/requirements.txt /BGEvr/requirements.txt
#COPY ./BGEvr/.env /BGEvr/.env 

RUN pip install -r /BGEvr/requirements.txt

COPY .dockerignore .
COPY ./BGEvr /BGEvr


CMD ["python","run_bot.py"]