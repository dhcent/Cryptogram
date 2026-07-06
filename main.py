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


alphabet = list("abcdefghijklmnopqrstuvwxyz")
quotes = ["Whether you think you can or you think you cannot, you are correct."]

selected_quote = random.choice(quotes)

# alphabet is now randomly shuffled
sattolo_cycle(alphabet)

new_quote = []

# iterate through and build the scrambled string based on the randomly shuffled alphabet
for i, char in enumerate(selected_quote):
    if char.isalpha():    
        new_quote.append(alphabet[ord(char.lower()) - ord("a")])
    else:
        new_quote.append(char)


# new_quote is now scrambled of the original
new_quote = "".join(new_quote)


print(new_quote)