import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="TFM MBIT",
        page_icon="",
    )


    st.write("# Stroke prediction in fibrillation pacients")

    st.sidebar.success("Check your probability to have a stroke.")

    st.markdown(
        """
La fibrilación auricular (FA) es una condición cardíaca común que 
puede tener graves implicaciones para la salud, en particular en lo que 
respecta a la posibilidad de sufrir un ictus. 
El ictus, también conocido como apoplejía, 
es un evento médico crítico que ocurre cuando el suministro de sangre 
al cerebro se ve interrumpido, generalmente debido a un coágulo sanguíneo. 
La FA es un factor de riesgo importante para el ictus.
    """
    )


if __name__ == "__main__":
    run()
