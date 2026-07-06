import streamlit as st
import pandas as pd
import numpy as np
import random
from logic import *

c = st.container()
c.write("HI")
st.title("Cryptograms :)")
st.markdown("test")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

alphabet = list("abcdefghijklmnopqrstuvwxyz")
quotes = ["Whether you think you can or you think you cannot, you are correct."]

selected_quote = random.choice(quotes)
sattolo_cycle(alphabet)

for c in selected_quote:
    pass 

print(alphabet)
# Creates a list of columns
cols = st.columns[10]

for i in range(cols):
    with cols[i]:
        letter = st.text_input(
            label = f"Letter {i}" #explains to user what input is for
            value = ""
            max_chars = 1
        )
