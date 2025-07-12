print('hello world')
print('Welcome Here')
print('Welcome Here')
print('Welcome Here')
num1 = 5
num2 = 3

sum = num1 + num2

print("The sum is:", sum)


import streamlit as st

USERNAME = "admin"
PASSWORD = "1234"

def login():
    st.title("🔐 Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.success("✅ Login Successful!")
        else:
            st.error("❌ Incorrect username or password")

login()

