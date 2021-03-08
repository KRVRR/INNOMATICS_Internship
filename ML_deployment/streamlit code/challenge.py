import streamlit as st
from sklearn.svm import SVC
from pickle import load
import numpy as np

def predict(arr):
  classifier=load(open('pickle/svm_rbf_model.pkl', 'rb'))
  prediction=classifier.predict(arr)
  return prediction


def main():
  col1=st.number_input('Col 1 value : ')
  col2=st.number_input('Col 2 value : ')
  arr = np.array([col1,col2]).reshape(1,-1)
  arr = arr.astype('float64')
  prediction = predict(arr)
  click = st.button('SUBMIT')
  if click:
          for i in prediction:
              if (i==0):
                  st.write('Class zero(0)')
              elif (i==1):
                  st.write('Class one(1)')
              else:
                  st.write('Sorry, your requirement cannot be fulfilled')

if(__name__=='__main__'):
  main()
