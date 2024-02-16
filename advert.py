#importing the neseceery
import pandas as pd
import numpy as np
import pypickle
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
import streamlit as st


loaded_model = pypickle.load('model.pkl')

def prediction(data):
     df = pd.DataFrame(data)


     num_data = df.values.reshape(1, -1)

     pred = loaded_model.predict(num_data)

     return f"The prediction of Product is{pred}"



def main():

     st.title("Sales Advert Prediction")

     Tv = st.number_input("what is the amount spent on tv advert")
     Radio = st.number_input("What is the amount spent on radio advert")
     Newspaper = st.number_input("What is the amount spent on newspaper advert")
    

     sales = " "

     if st.button("Result"):
          sales = prediction([[Tv, Radio, Newspaper]])
          

     st.success(sales)

if __name__ == "__main__":
     main()