import streamlit as st
import datetime
import time
import numpy as np

st.set_page_config(page_title="first Demo",page_icon=':tropical_drink:')

st.write("NO.1 你的心情指数")
agree = st.checkbox('选择你的心情指数:sparkles:')
if agree:
    n = st.slider("开心", 0, 100, 50, 1)
    if n < 50:
        st.write("请你喝杯奶茶，开心点")
    elif n < 90:
        st.write("每天都要保持这份开心")
    else:
        st.write("开心的冒泡泡了")



st.write('NO2.最爱的美食')
agree = st.checkbox('选择你的美食:sparkles:')
if agree:
    op = st.selectbox("请选择",('烧烤','奶茶','火锅',"烤鱼",'川菜','水果'))
    st.write('你选择',op)



st.write('NO.3 你的星座')
agree = st.checkbox('生日:sparkles:')
if agree:
    birthday=st.date_input('选择你的生日',datetime.date(2023,2,27))
    st.write('你的星座：')













