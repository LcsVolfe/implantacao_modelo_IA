import requests
import streamlit as st
from api_server.model_service import analyze_text
from src.utils import save_prediction, get_all_predictions
from src.auth import check_password
from api_server.dataset_service import load_dataset
from pathlib import Path

if not check_password():
    st.stop()

def _nova_analise():
    st.session_state.texto_analise = ''


def _call_model(texto: str):
    #response = requests.get(f'http://127.0.0.1:8000/predict_sentimental?message_text={texto}')
    #print(response)
    #result = response.json()

    result = analyze_text(texto)
    if result:
        analise = dict()
        analise['texto'] = texto

        st.write(f"Positivo: {round(result['positive'] * 100, 2)}%")
        st.write(f"Neutro: {round(result['neutral'] * 100, 2)}%")
        st.write(f"Negativo: {round(result['negative'] * 100, 2)}%")

        st.text("O resultado esta coerente?")
        col1, col2, col3 = st.columns([1, 1, 5])
        with col1:
            correct_prediction = st.button('👍🏻')
        with col2:
            wrong_prediction = st.button('👎🏻')

        if correct_prediction or wrong_prediction:
            message = "Muito obrigado pelo feedback"
            if wrong_prediction:
                message += ", iremos usar esses dados para melhorar as predições"
            message += "."

            if correct_prediction:
                analise['CorrectPrediction'] = True
            elif wrong_prediction:
                analise['CorrectPrediction'] = False

            st.write(message)
            save_prediction(analise)


txt = st.text_input("Insira o texto:", key='texto_analise')
if txt:
    _call_model(txt)
    st.button('Nova analise', on_click=lambda: _nova_analise())



accuracy_predictions_on = st.toggle('Exibir acurácia', value=True)

if accuracy_predictions_on:
    predictions = get_all_predictions()
    num_total_predictions = len(predictions)

    accuracy_hist = [0]
    correct_predictions = 0
    previous_accuracy = 0
    for index, passageiro in enumerate(predictions):
        total = index + 1
        if passageiro['CorrectPrediction']:
            correct_predictions += 1

        temp_accuracy = correct_predictions / total if total else 0
        accuracy_hist.append(round(temp_accuracy, 2))

        if total > 1:
            delta_accuracy = round(temp_accuracy - previous_accuracy, 2)
        else:
            delta_accuracy = 0

        previous_accuracy = temp_accuracy

    accuracy = correct_predictions / num_total_predictions if num_total_predictions else 0

    st.metric(label='Acurácia', value=round(accuracy, 2), delta=delta_accuracy)
    st.write(f'Total de feedbacks: {num_total_predictions}')
    st.subheader("Histórico de acurácia")
    st.line_chart(accuracy_hist)
