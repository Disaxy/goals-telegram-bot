FROM python:3.8-alpine

WORKDIR /bot

COPY *.py, requirements.txt, *.sqlite, *.data ./

ENV TZ=Europe/Moscow

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    pip install -Ur requirements.txt && \
    apt-get update && apt-get install sqlite3

ENTRYPOINT ["python", "bot.py"]