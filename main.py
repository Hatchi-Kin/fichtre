import streamlit as st
import pandas as pd


df = pd.read_csv('data.csv')
random_row = df.sample(n=1)

random_word = random_row.iloc[0, 0]
random_definition = random_row.iloc[0, 1]


st.title("Nous vivons vraiment dans une saucisse.")
st.header("Vous avez des valeurs et des soft-skills qui font de vous le convive par excellence.:hibiscus:")
st.subheader("En toute bienséance, vous ne sauriez choquer vos contemporains par un langage mal à propos.")
st.write("Toutefois, la frustration et la colère s'accumulent en vous, et vous vous laisseriez bien tenter par un petit 'gros-mot'.")
st.write("Vous n'avez pas l'habitude et ne savez pas par où commencer ?:innocent:")


dirty_css_tech = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #EB804C;
}
</style>""", unsafe_allow_html=True)

if st.button('Cliquez ici !'):
    st.write(random_word)
    st.write(random_definition)
    st.write("n'abusez pas des bonnes choses, on vit tout de même dans une saucisse.")
else:
    st.write("Pas les mamans :no_entry:")
