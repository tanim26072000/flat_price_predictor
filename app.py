import streamlit as st
import pandas as pd
import pickle

st.title('Flat Rent Predictor within Dhaka')
with open('ridgemodel.pkl', 'rb') as f:
    model = pickle.load(f)
df = pd.read_csv('cleaned_data.csv')
location = st.selectbox('type your desired location:',
                        df['Location'].unique())
bed = st.text_input("Enter required no. of bedroom:")
bath = st.text_input("Enter required no. of bathroom:")
size = st.text_input("Enter required size (in sqft):")


if st.button('Predict'):
    if bed == "" or bath == "" or size == '':
        if (bed == ''):
            st.warning("No. of bed can't be empty")
        if (bath == ''):
            st.warning("No. of bath can't be empty")
        if (size == ''):
            st.warning("size can't be empty")
    else:
        bed, bath, size = map(float, [bed, bath, size])
        test = {'Location': location, 'Bed': bed, 'Bath': bath, 'Area': size}
        x_test = pd.DataFrame(test, index=[0])
        prediction = model.predict(x_test)
        p_int = int(prediction[0])
        crore = p_int//100000
        lakh = p_int % 100000
        lakh = lakh//1000
        s = f'The rent of a flat with desired features in desired location can be around'
        s1 = ''
        s2 = ''
        if (crore > 0):
            s1 = f' {crore} lakh(s)'
            s = s+s1
        if (lakh > 0):
            s2 = f' {lakh} Thousand(s)'
            s = s+s2
        st.write(s)