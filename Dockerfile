FROM python:3.8-alpine

WORKDIR /home

ENV TZ=Europe/Moscow

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install -Ur requairements.txt && apt-get update && apt-get install sqlite3

COPY *.py, requairements.txt, *.sqlite, *.data ./

ENTRYPOINT ["python", "bot.py"]