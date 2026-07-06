import streamlit as st
import pandas as pd
import numpy as np
import random




def sattolo_cycle(items) -> None:
    """Sattolo's algorithm."""
    i = len(items)
    while i > 1:
        i = i - 1
        j = random.randrange(i)  # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]

c = st.container()
c.write("HI")
st.title("Cryptograms :)")
<<<<<<< HEAD
st.markdown("tomato")
=======
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
