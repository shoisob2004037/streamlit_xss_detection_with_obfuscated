# -*- coding: utf-8 -*-
"""
Created by Mahadi Hasan Shaisob ✨
Modernized XSS Prediction App (Streamlit) - Character n-gram version
"""

import pickle
import streamlit as st

# Load char-level vectorizer and model
loaded_model = pickle.load(open("trained_xss_char.sav", 'rb'))
tfidf_vectorizer_char = pickle.load(open("tfidf_vectorizer_char.sav", 'rb'))

def xss_prediction(payload):
    # Char-level n-gram: no manual tokenization needed
    features = tfidf_vectorizer_char.transform([payload])
    prediction = loaded_model.predict(features)
    if prediction[0] == 1:
        return '🔴 This payload is XSS (Malicious)'
    else:
        return '🟢 This payload is Benign (Not XSS)'

def main():
    st.set_page_config(page_title="XSS Prediction App", page_icon="🛡️", layout="centered")

    st.markdown("""
        <style>
        .stApp {
            background-image: linear-gradient(135deg, #D6E6F2, #BFD7ED, #9FB4CE, #607EAA);
            background-attachment: fixed;
            color: #003366;
            font-family: 'Segoe UI', sans-serif;
        }
        h1 {
            text-align: center;
            color: #003366;
        }
        .css-18e3th9 {
            padding-top: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1>🛡️ XSS Payload Detection Web App</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Enter a suspected XSS payload below to check if it's malicious.</p>", unsafe_allow_html=True)

    st.sidebar.header("About")
    st.sidebar.info(
        """
        This web app predicts whether a payload is a harmful XSS attempt.
        Built with ❤️ using **Streamlit** and **Machine Learning**.
        """
    )

    st.subheader("💻 Enter Payload Below:")

    payload = st.text_area("Paste XSS payload here", "", height=150)

    diagnosis = ""
    if st.button('🔍 Check XSS'):
        if payload.strip():
            diagnosis = xss_prediction(payload.strip())

    if diagnosis:
        if 'Benign' in diagnosis:
            st.success(diagnosis)
        else:
            st.error(diagnosis)

    st.markdown("---")
    st.markdown("<p style='text-align:center; font-size:13px;'>Made with 💙 by Mahadi Hasan Shaisob</p>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
