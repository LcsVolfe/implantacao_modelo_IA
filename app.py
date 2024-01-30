import streamlit as st
import matplotlib.pyplot as plt
from src.auth import check_password
from src.data_handler import read_data
from src.model import analyze_text

# if not check_password():
#     st.stop()


def _call_model(text):
    result = analyze_text(text)
    st.text(result)

text = st.text_input('text')

st.button('Analisar', on_click=_call_model(text))

# df = read_data('src/test.csv')
# st.dataframe(df)
#
# st.header("Histograma idades")
#
# fig = plt.figure()
# plt.hist(df['Age'], bins=30)
# plt.xlabel('Idade')
# plt.ylabel('Quantidade')
# st.pyplot(fig)
#
# st.header("Sobreviventes")
# st.bar_chart(df.Pclass.value_counts())
