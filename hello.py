import streamlit as st

st.set_page_config(
    page_title='Hello',
    page_icon="👋"
)

def intro():
    import streamlit as st

    st.write('# Sandy first test')

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.

        **👈 Select a demo from the dropdown on the left** to see some examples
        of what Streamlit can do!

        ### Want to learn more?

        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)

        ### See more complex demos

        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )

def bmi_demo():
    import streamlit as st

    st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
    height = st.slider("身高 (cm)", 100, 250, 170, 1)
    st.write('你的身高：',height)

    wet = st.slider("体重 (kg)", 40, 200, 70, 1)
    st.write('你的体重：', wet)

    # Calculate BMI
    bmi = round(wet / ((height / 100) ** 2), 2)

    # Display BMI
    st.write("BMI:", bmi)

    # Evaluate BMI and display results
    if bmi < 18.5:
        st.write("你有点瘦了，多吃点")
    elif bmi < 25:
        st.write("恭喜你，正常体重.")
    elif bmi < 30:
        st.write("有点偏胖了，运动运动.")
    else:
        st.write("超重了，管住嘴迈开腿.")


def ball_demo():
    import streamlit as st
    st.markdown(f'# {list(page_names_to_funcs.keys())[2]}')
    st.button('重来一次')
    st.balloons()



def snow_demo():
    import streamlit as st
    st.markdown(f'# {list(page_names_to_funcs.keys())[3]}')
    st.button('重来一次')
    st.snow()



page_names_to_funcs = {
    "—": intro,
    "BMI": bmi_demo,
    "小气球🎈": ball_demo,
    "雪花❄": snow_demo
}


demo_name = st.sidebar.selectbox("请选择", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()

