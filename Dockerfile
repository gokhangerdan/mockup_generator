FROM python:3.8-slim

EXPOSE 5000

WORKDIR /app

ADD hello.py /app
ADD requirements.txt /app
ADD mockup_file.json /app

RUN pip install -r requirements.txt

ENTRYPOINT ["flask", "--app", "hello", "run"]