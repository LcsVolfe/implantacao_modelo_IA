FROM python:3.11-slim
LABEL authors="lucas.volfe"

RUN mkdir /opt/app

COPY src /opt/app/
COPY predictions.json requirements.txt app.py .streamlit /opt/app/

RUN pip install -r requirements.txt

EXPOSE 8051

ENTRYPOINT ["streamlit", "run", "app.py"]
