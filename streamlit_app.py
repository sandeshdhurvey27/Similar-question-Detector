import streamlit as st
import helper
import pickle
model=pickle.load(open('model.pkl','rb'))
st.header('Similary question Detector')

q1 = st.text_input('Enter your question 1')
q2 = st.text_input('Enter your question2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('Similary question')
    else:
        st.header('differnt question')