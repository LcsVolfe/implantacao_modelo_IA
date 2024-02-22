FROM python:3.11-slim
LABEL authors="lucas.volfe"

RUN mkdir /opt/app

COPY src /opt/app/src
COPY predictions.json requirements.txt app.py .streamlit /opt/app/

RUN pip install -r /opt/app/requirements.txt

WORKDIR /opt/app
ENV STREAMLIT_SERVER_PORT=80
EXPOSE 80

ENTRYPOINT ["streamlit", "run", "app.py"]
