import streamlit as st

from src import utils
from src.auth import check_password
from src.model import analyze_text


# if not check_password():
#     st.stop()

def _nova_analise():
    st.session_state.texto_analise = ''


def _call_model(texto: str):
    result = analyze_text(texto)
    if result:
        analise = dict()
        analise['texto'] = texto

        st.write(f"- Neutral: {result['neutral']}")
        st.write(f"- Positive: {result['positive']}")
        st.write(f"- Negative: {result['negative']}")

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
            utils.save_prediction(analise)


txt = st.text_input("Insira o texto:", key='texto_analise')
if txt:
    _call_model(txt)
    st.button('Nova analise', on_click=lambda: _nova_analise())

accuracy_predictions_on = st.toggle('Exibir acurácia', value=True)

if accuracy_predictions_on:
    predictions = utils.get_all_predictions()
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
