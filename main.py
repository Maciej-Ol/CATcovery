import streamlit as st
import pandas as pd
import pickle
from fileinput import filename
import names
from io import StringIO
from PIL import Image
from PIL import ImageDraw
import fastai
from fastai.vision.all import *
from fastai.vision.widgets import *
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
from io import BytesIO

model_filename = "model.pkl"
#miejsce na wgranie modeli
cat_model = pickle.load(open(model_filename, 'rb'))

@st.cache
def get_cat_to_dowland(picture,cat_name,cat_age,rasa, score):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    #Bierze obraz i z dołu dodaje imię i wiek
    cat_picture = Image.open(picture)
    bottom=40
    width, height = cat_picture.size
    #print(height)
    new_height = height + bottom
    result=Image.new(cat_picture.mode, (cat_picture.size[0], new_height), (255, 255, 255))
    result.paste(cat_picture, (0, 0))
    I1 = ImageDraw.Draw(result)
    I1.text((20, height+15), f"Name: {cat_name}, Age: {cat_age}, Rase: {rasa}, Score: {score}", fill=(0, 0, 0))
    result.save("cat_picture.jpg")
    #with BytesIO() as f:
    #    result.save(f, format='JPEG')
    #    f.seek(0)
    #    ima_jpg = Image.open(f)
    #    ima_jpg.load()
    #return ima_jpg
    

def main():
    if 'name' not in st.session_state:
        st.session_state['name'] = ''
    # if 'second_stage' not in st.session_state:
    #     st.session_state['second_stage'] = False

    overview = st.container()
    uploadfile = st.container()
    left2, right2 = st.columns(2)
    foto = st.container()
    cat_rest = st.container()
    
    with overview:
        #tutaj pobiera zdjęcie z kamery lub z dysku
        st.title("App to discover your cat")
        option = st.selectbox(
        'Take or upload a picture',
        ["Upload","Take"])
        if option=="Take":
            st.camera_input("Take a picture", key= "cat_picture")
        else:
            st.file_uploader("Choose a file", type = ['jpg','png'], key= "cat_picture")
        #st.session_state['second_stage']=st.button('DISC(CAT)COVER!!!')

    with uploadfile:
        #zabawa ze zdjęciem, które już jest
            #Spinner na razie nie działa
            #st.spinner(text="In progress...")
            #time.sleep(5)
        if st.session_state['cat_picture'] is not None:
            bytes_data = st.session_state['cat_picture'].getvalue()
            #Miejsce na predykcje różnych modeli co do zdjęcia
            predictions = cat_model.predict(bytes_data)
            st.session_state['score'] = score = round(predictions[2].numpy()[0]*100,3)
            st.session_state['pred'] = predictions[0]
            #Wrzucanie różnych metryk
            left2.metric(label="Rasa", value=predictions[0]) #predictions[0]
            right2.metric(label="Prawdopodobieństwo", value=score) #score
            foto.image(bytes_data, caption='Uploaded Cat.', use_column_width=True)
            #st.balloons()
        else:
            st.error("Najpierw załaduj zdjęcie", icon="🚨")
    with cat_rest:
        if st.session_state['cat_picture'] is not None: 
            if st.button('Generate a name'):
                st.session_state['name'] = generated_name = names.get_first_name()
            text_name = st.text_input('Your cat name', st.session_state['name'])
            if text_name is not None and text_name !='':
                st.session_state['name'] = text_name
            age = st.slider('Your cat age', 0, 20, 1)
            st.write("More information about your cat:")
            st.write(st.session_state['name']," it's a fun name for a cat!")
            st.write("Age: ", age)
            get_cat_to_dowland(st.session_state['cat_picture'],st.session_state['name'],
                               age,predictions[0],score)
            with open("cat_picture.jpg","rb") as file:
                btn=st.download_button(
                    label="Download your cat",
                    data=file,
                    file_name='cat.jpg',
                    mime='image/jpg',)            


if __name__=="__main__":
    main()
    
