import streamlit as st

st.title("Simple App")
st.header("Streamlit App 개발 환경 설정중")
st.text("테스트 용 텍스트 ")

k=st.text_input("하이")
st.write(k)

print(k)
