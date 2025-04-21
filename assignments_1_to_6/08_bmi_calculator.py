import streamlit as st

st.title("BMI Calculator")

height=st.slider("Enter Your Height in (cm):",100,250,175)
weight= st.slider("Enter Your weight in (kg):",40 ,200,70)

bmi= weight / ((height/100)**2)

st.success(f"Your BMI is {bmi:.2f}")
st.write("### BMI categories ###")
st.write("-Underweight: BMI less than 18.5")
st.write("-Normal: BMI between 18.5 and 24.9")
st.write("-Overwight: BMI between 25 and 29.9")
st.write("-Obesity: BMI 30 or greater")
