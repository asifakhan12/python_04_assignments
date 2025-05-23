import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Simple Data Dashboard")
    uploaded_file = st.file_uploader("Choose a CSV File", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.subheader("Data Preview")
        st.write(df.head())

        st.subheader("Data Summary")
        st.write(df.describe())

        st.subheader("Filter Data")
        columns = df.columns.tolist()
        selected_column = st.selectbox("Select Columns to Filter by", columns)
        unique_values = df[selected_column].unique()
        selected_value = st.selectbox("select Value", unique_values)
        
        filtered_df=df[df[selected_column]==selected_value]
        st.write(filtered_df)
        
        st.subheader("Plot Data")
        x_column=st.selectbox("Select x-axis Column",columns)
        y_column=st.selectbox("Select y-axis Column",columns)
        if st.button("Generate Plot"):
            st.line_chart(filtered_df.set_index(x_column)[y_column])
        else:
            st.write("Waiting on file upload...")

if __name__ == "__main__":
    main()
