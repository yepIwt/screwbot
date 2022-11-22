FROM python:3.9.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV BOT_TOKEN=""

COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","main.py"]