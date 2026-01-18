import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng


st.title("신규자동차등록현황")


df = pd.DataFrame(
    rng(0).standard_normal((10, 20)), columns=("col %d" % i for i in range(20))
)

st.dataframe(df.style.highlight_max(axis=0))