from distutils.command.upload import upload
from turtle import up
import streamlit as st
import pandas as pd
import seaborn as sns



st.title("Data Analysis")
st.subheader("Data Analysis Using Python & Streamlit")

upload = st.file_uploader("Upload Your Dataset (In CSV Format)")

if upload is not None:
    data = pd.read_csv(upload)


if upload is not None:
    if st.checkbox("Preview Dataset"):

        if st.button("Head"):
            st.write(data.head())

        if st.button("Tail"):
            st.write(data.tail())     



if upload is not None:
    if st.checkbox("DataType of Each Column"):
        st.text("DataType")
        st.write(data.dtypes.astype(str))


if upload is not None:

    data_shape  = st.radio("What Dimension Do You Want To Check?" , ('Rows'  , 'Columns'))

    if data_shape == 'Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])

    if data_shape == 'Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])     



if upload is not None:
    test = data.isnull().values.any()
    if test == True:
        if st.checkbox("Null Values in th edataset"):
            sns.heatmap(data.isnull())
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
    else:
        st.success("Congratualation!!! , No Missing Values")


if upload is not None:
    test = data.duplicated().any()
    if test == True:
        st.warning("This Dataset Contains Some Duplicate Values")
        dup = st.selectbox("Do You Want to Remove Duplicate Values?",("Select One", "Yes", "No"))
        if dup == 'Yes':
            data = data.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup == "No":
            st.text("Ok No Problem")     

if upload is not None:
    if st.checkbox("Summary of the Dataset"):
        st.write(data.describe(include='all').astype(str))




if st.button("About App"):
    st.text("Built With Streamlit")
    st.text("Thanks To Streamlit")

if st.checkbox("By"):
    st.success("Happeace Codes")    














