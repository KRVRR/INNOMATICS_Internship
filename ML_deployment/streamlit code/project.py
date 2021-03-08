import streamlit as st
import challenge

def main():
  st.header("ML Model DEPLOYMENT CHALLENGE")
  st.subheader("SVM(SVC)-RBF Predictor")
  st.image('./innomatics.png')
  challenge.main()

if(__name__=='__main__'):
  main()
