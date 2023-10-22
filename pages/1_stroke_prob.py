# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any

import numpy as np
import pickle
import streamlit as st

def stroke_prob() -> None:

    # Interactive Streamlit elements, like these sliders, return their value.
    # This gives you an extremely simple interaction model.
    iterations_1 = st.sidebar.number_input("Edad:")
    iterations_2 = st.sidebar.number_input("Sexo:")
    iterations_3 = st.sidebar.number_input("Visitas al hospital en el último año:")
    iterations_4 = st.sidebar.number_input("¿Has tenido fibrilaciones?")
    
    with open("/workspaces/tfm-mbit/pages/modelo.pkl", 'rb') as archivo:
        modelo_cargado = pickle.load(archivo)
    
    input_data = [[iterations_1, iterations_2, iterations_3, iterations_4]]
    output = modelo_cargado.predict(input_data)
    if iterations_1 != 0 and iterations_2 != 0 and iterations_3 != 0 and iterations_4 != 0:
        if output == 0:
            st.write("No parece haber probabilidad de Ictus, aunque siempre es recomendable una revisión médica.")
        elif output == 1:
            st.write("Hay probabilidad de Ictus en el proximo año. Te recomendamos que durante el próximo año estés pendiente de tu salud y que te hagas un reconocimiento médico cuanto antes.")
    else:
        print("Introduzca sus datos en la barra de la izquierda por favor.")        

st.set_page_config(page_title="Stroke Probability", page_icon="📹")
st.markdown("# Stroke Prob")
st.sidebar.header("Stroke Prob")
st.write(
    """Esta aplicación calcula si una persona tiene probabilidad de tener un ictus en el próximo año desde su última fibrilación."""
)

if __name__ == '__main__':
    stroke_prob()
