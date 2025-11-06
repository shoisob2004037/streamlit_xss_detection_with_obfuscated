# -*- coding: utf-8 -*-
"""
XSS Prediction Script (Character n-gram version)
"""

import pickle

# Load saved model (.sav) and char-level vectorizer
loaded_model = pickle.load(open(r"C:\Users\Asus\Desktop\xss_streamlit\trained_xss_char.sav", 'rb'))
tfidf_vectorizer_char = pickle.load(open(r"C:\Users\Asus\Desktop\xss_streamlit\tfidf_vectorizer_char.sav", 'rb'))

def xss_prediction(payload):
    """
    Predict XSS (1) or benign (0) using char-level TF-IDF.
    Args: payload (str)
    Returns: str result
    """
    # Character n-gram vectorization (no tokenization)
    features = tfidf_vectorizer_char.transform([payload])
    prediction = loaded_model.predict(features)
    if prediction[0] == 1:
        return '🔴 This payload is XSS (Malicious)'
    else:
        return '🟢 This payload is Benign (Not XSS)'

# Example usage
if __name__ == '__main__':
    test_payload = "<img src=x onerror=alert(1)>"
    print(xss_prediction(test_payload))
