import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.header("Write Demo")

# Write can contain styles and markdown
st.write("Hello *World* :sunglasses:")

# Write can also contain numbers
st.write(1234)

# Write can also contain dataframes
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Write displays elements in a column
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Write can also display altair charts
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)