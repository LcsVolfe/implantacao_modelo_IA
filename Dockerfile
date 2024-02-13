FROM python3.9
LABEL authors="lucas.volfe"

RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "app.py"]