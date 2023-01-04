import streamlit as st
import pandas as pd
from io import StringIO
import fastai
from fastai.vision.all import *
from fastai.vision.widgets import *
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

#miejsce na wgranie modeli
#model=load_learner("model.pkl")

def main():
    if 'recent' not in st.session_state:
        st.session_state['recent'] = 0
    overview = st.container()
    uploadfile = st.container()
    left2, right2 = st.columns(2)
    foto = st.container()

    
    with overview:
        st.title("App to discover your cat")
        option = st.selectbox(
        'Take or upload a picture',
        ["Upload","Take"])
        if option=="Take":
            cat_picture = st.camera_input("Take a picture")
        else:
            cat_picture = st.file_uploader("Choose a file", type = ['jpg','png'])

    with uploadfile:
        if st.button('DISC(CAT)COVER!!!'):
            if cat_picture is not None:
                bytes_data = cat_picture.getvalue()
                #Miejsce na predykcje różnych modeli co do zdjęcia
                #predictions = model.predict(bytes_data)
                #score = round(predictions[2].numpy()[0]*100,3)

                #Wrzucanie różnych metryk
                left2.metric(label="Rasa", value=predictions[0])
                right2.metric(label="Prawdopodobieństwo", value=score)
                foto.image(cat_picture.getvalue())
            else:
                st.write("First upload a picture")
                


if __name__=="__main__":
    main()
    
