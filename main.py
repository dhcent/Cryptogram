import streamlit as st
import pandas as pd
import numpy as np
import random
from logic import *

st.markdown(
    """
    <style>
        .stApp {
            background-color: #ADD8E6
            }
    <\style>
    """,
    unsafe_allow_html = True
)


c = st.container()
c.write("HI")
st.title("Cryptograms :)")
st.markdown("test")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})


print(new_quote)

str_len = len(new_quote)
# Creates a list of columns
cols = st.columns(str_len)
# For each column, create a text input box.
for i in range(str_len):
    with cols[i]:
        letter = st.text_input(
            label = f"Letter {i + 1}", #explains to user what input is for
            value = "",
            max_chars = 1,
            label_visibility = "hidden",
        )

