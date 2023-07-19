#!/usr/bin/env python
# coding: utf-8

# In[9]:


import streamlit as st
import pandas as pd
import pickle

# Load the trained Gradient Boosting Regressor model
model_filename = 'pricemodel.pkl'  # Replace with the filename of your saved model
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Function to predict price based on input features
def predict_price(carat, cut, color, clarity, depth, table, x, y, z):
    input_data = pd.DataFrame({
        'carat': [carat],
        'cut': [cut],
        'color': [color],
        'clarity': [clarity],
        'depth': [depth],
        'table': [table],
        'x': [x],
        'y': [y],
        'z': [z]
    })

    prediction = model.predict(input_data)
    return prediction[0]

# Create a Streamlit web app
def main():
    st.title('Diamond Price Prediction')

    st.write('Please enter the following features to get the price prediction.')

    carat = st.number_input('Carat', min_value=0.2, max_value=5.01, value=1.0, step=0.01)
    cut = st.selectbox('Cut', [1,2,3,4,5])
    color = st.selectbox('Color', [1,2,3,4,5,6,7])
    clarity = st.selectbox('Clarity', [1,2,3,4,5,6,7,8])
    depth = st.number_input('Depth', min_value=43.0, max_value=79.0, value=60.0, step=0.1)
    table = st.number_input('Table', min_value=43.0, max_value=95.0, value=55.0, step=0.1)
    x = st.number_input('x', min_value=0.0, max_value=10.74, value=5.0, step=0.01)
    y = st.number_input('y', min_value=0.0, max_value=58.9, value=5.0, step=0.01)
    z = st.number_input('z', min_value=0.0, max_value=31.8, value=5.0, step=0.01)

    if st.button('Predict'):
        prediction = predict_price(carat, cut, color, clarity, depth, table, x, y, z)
        st.write(f'Predicted Price: ${prediction:.2f}')

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




