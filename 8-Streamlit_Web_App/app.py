
##################################################################################
##############Import libraries required###########################################
##################################################################################
import pandas as pd 
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

##################################################################################
##############Title and Subheader###########################################
##################################################################################
st.title("Data Analysis")
st.subheader("Data Analysis using Pandas and Streamlit")

##################################################################################
##############Upload any Dataset###########################################
##################################################################################
upload = st.file_uploader("Upload your dataset (.csv file)")
if upload is not None:
    df = pd.read_csv(upload)


##################################################################################
##############Show Dataset###########################################
##################################################################################
if st.checkbox("Preview Dataset"):
    if st.button("Head"):
        st.write(df.head(5))
    
    if st.button("Tail"):
        st.write(df.tail(5))


##################################################################################
##############Check Data Type of Each Column###########################################
##################################################################################
if upload is not None:
    if st.checkbox("Datatype of each columns"):
        st.text("Data Types")
        st.write(df.dtypes)

##################################################################################
##############Find Shape of Our Dataset###########################################
##################################################################################
if upload is not None:
    if st.checkbox("Shape of Dataset"):
        data_dimension = st.radio("What dimension do you want to check?",("Rows","Columns"))
        if data_dimension == "Rows":
            st.write(df.shape[0])
        else:
            st.write(df.shape[1])

##################################################################################
##############Find Null Values in the datset###########################################
##################################################################################
if upload is not None:
    status = df.isnull().values.any()
    if status == True:
        if st.checkbox("Null values in the dataset"):
            fig, ax = plt.subplots()
            sns.heatmap(df.isnull())
            st.pyplot(fig)
    else:
        st.success("No null values found.")

##################################################################################
##############Find duplicates in the dataset###########################################
##################################################################################
if upload is not None:
    duplicated=df.duplicated().any()
    if duplicated==True:
        st.warning("Dataset contains duplicate values")
        dup=st.selectbox("Do you want to remove duplicate values?",\
            ("Select one option.","Yes","No"))
        if dup=="Yes":
            df.drop_duplicates()
            st.text("Duplicate values are removed.")
        if dup=="No":
            st.warning("Suit yourself idiot!")

##################################################################################
##############Get overall statistics###########################################
##################################################################################
if upload is not None:
    if st.checkbox("Summary of the Dataset"):
        st.write(df.describe(include='all'))


##################################################################################
##############About App###########################################
##################################################################################
if st.button("About App"):
    st.text("Bhai dekhein, rishta info tau deni nai about section mein")
    st.text("Aur asli app hai nai jo info dun")
    st.text("Chal bhaag yahan se")
    