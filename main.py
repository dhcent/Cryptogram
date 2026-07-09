import streamlit as st
import pandas as pd
import numpy as np
import random
import importlib
import logic
importlib.reload(logic)

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

# USED AI TO SET UP THE DISPLAY. TAKE A BRIEF LOOK
st.markdown(
    """
    <style>
    div[data-testid="stTextInput"] input {
        width: 32px !important;
        min-width: 32px !important;
        max-width: 32px !important;
        height: 40px !important;
        padding: 0 !important;
        margin: 0 auto !important;
        text-align: center !important;
        font-size: 22px !important;
        font-weight: 600 !important;
        font-color: 
        color: #222 !important;
        background-color: transparent !important;
        border: none !important;
        border-bottom: 3px solid #333 !important;
        border-radius: 0 !important;
        box-shadow: none !important;
    }
    div[data-testid="stTextInput"] input:focus {
        border-bottom: 3px solid #1a73e8 !important;
        outline: none !important;
    }

    /* Force every column to a fixed pixel width, regardless of row weight sums */
    div[data-testid="stHorizontalBlock"] div[data-testid="stColumn"] {
        flex: 0 0 32px !important;
        width: 32px !important;
        min-width: 32px !important;
        max-width: 32px !important;
        display: flex !important;
        justify-content: center !important;
    }

    /* Word-gap columns get a smaller fixed width */
    div[data-testid="stColumn"]:has(.gap-col) {
        flex: 0 0 16px !important;
        width: 16px !important;
        min-width: 16px !important;
        max-width: 16px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

c = st.container()
st.title("Cryptograms :)")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})


alphabet = list("abcdefghijklmnopqrstuvwxyz")
quotes = ["Whether you think you can or you think you cannot, you are correct."]

selected_quote = random.choice(quotes)

# alphabet is now randomly shuffled
logic.sattolo_cycle(alphabet)

new_quote = []

print(alphabet)

# iterate through and build the scrambled string based on the randomly shuffled alphabet
for i, char in enumerate(selected_quote):
    if char.isalpha():    
        new_quote.append(alphabet[ord(char.lower()) - ord("a")])
    else:
        new_quote.append(char)


# new_quote is now scrambled of the original
new_quote = "".join(new_quote)


print(new_quote)

logic.render_cryptogram(new_quote, 30)
