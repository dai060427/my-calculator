import streamlit as st

st.title("🧮 我的小计算器")

num1 = st.number_input("请输入第一个数字", value=0.0)
num2 = st.number_input("请输入第二个数字", value=0.0)

st.subheader("计算结果：")
st.write("加法：", num1 + num2)
st.write("减法：", num1 - num2)
st.write("乘法：", num1 * num2)

if num2 != 0:
    st.write("除法：", num1 / num2)
else:
    st.write("除法：除数不能为 0")