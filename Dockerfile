FROM python:3.9

ENV USER_NAME=forwarder
ARG PROJECT_DIR=/app

RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev && useradd $USER_NAME

WORKDIR $PROJECT_DIR

COPY --chown=$USER_NAME:$USER_NAME requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

USER $USER_NAME

COPY --chown=$USER_NAME:$USER_NAME . ./

CMD [ "python","main.py" ]