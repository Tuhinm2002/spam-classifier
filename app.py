import streamlit as st
import pickle


class app:

    st.markdown(""" # SPAM RECOGNITION """)

    def __init__(self):
        self.message=st.text_area(label="Enter message",key=1)
        self.vect=pickle.load(open("Count_vector.pkl","rb"))
        self.model=pickle.load(open("Model_classifier_spam.pkl","rb"))



    def predictor_(self):
        self.text=self.vect.transform([self.message]).toarray()
        self.button1=st.button("Predict")
        if self.button1:
            self.prediction=self.model.predict(self.text)
            if self.prediction[0]==1:
                st.write("IT IS A SPAM")
            else:
                st.write("IT IS NOT A SPAM")


App=app()
App.predictor_()




