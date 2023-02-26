import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.set_page_config(page_title="second Demo",page_icon=':tropical_drink:')

# Create some sample data
data = pd.DataFrame({
    'x': range(50),
    'y1': np.random.randn(50).cumsum(),
    'y2': np.random.randn(50).cumsum()
})

# Define the Altair charts
line_chart = alt.Chart(data).mark_line().encode(
    x='x',
    y='y1'
).properties(
    width=600,
    height=300
)

bar_chart = alt.Chart(data).mark_bar().encode(
    x='x',
    y='y2'
).properties(
    width=600,
    height=300
)


# Display the charts
st.write("折线图")
st.altair_chart(line_chart)

st.write("条形图")
st.altair_chart(bar_chart)

