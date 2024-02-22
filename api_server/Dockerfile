FROM python:3.11-slim
LABEL authors="lucas.volfe"

RUN mkdir /opt/app
WORKDIR /opt/app

COPY . /opt/app/

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn", "api:api"]


