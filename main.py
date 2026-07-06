import streamlit as st
import pandas as pd
import numpy as np


c = st.container()
c.write("HI")
st.title("Cryptograms :)")
st.markdown("test")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df