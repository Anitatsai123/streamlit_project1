import streamlit as st
from firebase_admin import credentials
from firebase_admin import firestore
import time

st.title("光線和距離即時監控")

def downloadData(): #function, not object method
    print("下載資料")


