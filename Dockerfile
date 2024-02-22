FROM python:3.11-slim
LABEL authors="lucas.volfe"

RUN mkdir /opt/app
WORKDIR /opt/app
#COPY api_server src /opt/app/
#COPY predictions.json requirements.txt app.py .streamlit /opt/app/
COPY . /opt/app/

RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 8051

ENTRYPOINT ["uvicorn", "api:api", "--reload"]
ENTRYPOINT ["streamlit", "run", "app.py"]


