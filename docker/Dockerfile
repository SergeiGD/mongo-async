FROM python:3.11-alpine3.20

WORKDIR /app


RUN apk update && apk add gcc python3-dev musl-dev

COPY ./src /app/src/
COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

COPY ./docker/ /app/docker/

RUN addgroup --system app && adduser -S app -G app
RUN chown -R app:app /app
RUN chmod +x /app/docker/entrypoint.sh

ENTRYPOINT ["sh", "/app/docker/entrypoint.sh"]