import streamlit as st
import pandas as pd
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

#miejsce na wgranie modeli
#model=load_learner("model.pkl")

@st.cache
def get_cat_to_dowland(picture,cat_name,cat_age):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    #Bierze obraz i z dołu dodaje imię i wiek
    cat_picture = Image.open(picture)
    bottom=100
    width, height = cat_picture.size
    print(height)
    new_height = height + bottom
    result=Image.new(cat_picture.mode, (cat_picture.size[0], new_height), (255, 255, 255))
    result.paste(cat_picture, (0, 0))
    I1 = ImageDraw.Draw(result)
    I1.text((20, height+20), f"Name: {cat_name}, Age: {cat_age}", fill=(0, 0, 0))
    result.save("cat_picture.jpg")
    #with BytesIO() as f:
    #    result.save(f, format='JPEG')
    #    f.seek(0)
    #    ima_jpg = Image.open(f)
    #    ima_jpg.load()
    #return ima_jpg
    

def main():
    if 'recent' not in st.session_state:
        st.session_state['recent'] = 0
    if 'second_stage' not in st.session_state:
        st.session_state['second_stage'] = False

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
            cat_picture = st.camera_input("Take a picture")
        else:
            cat_picture = st.file_uploader("Choose a file", type = ['jpg','png'])
        st.session_state['second_stage']=st.button('DISC(CAT)COVER!!!')

    with uploadfile:
        #zabawa ze zdjęciem, które już jest
        if st.session_state['second_stage']:
            #Spinner na razienie działa
            #st.spinner(text="In progress...")
            #time.sleep(5)
            if cat_picture is not None:
                bytes_data = cat_picture.getvalue()
                #Miejsce na predykcje różnych modeli co do zdjęcia
                #predictions = model.predict(bytes_data)
                #score = round(predictions[2].numpy()[0]*100,3)

                #Wrzucanie różnych metryk
                left2.metric(label="Rasa", value=12) #predictions[0]
                right2.metric(label="Prawdopodobieństwo", value=145) #score
                foto.image(bytes_data, caption='Uploaded Cat.', use_column_width=True)
                st.balloons()
            else:
                st.error("Najpierw załaduj zdjęcie", icon="🚨")
    #Tu się coś wywala, bo jak zmieni się name albo age, to znika wszystko z uploadfile i cat_rest
    #Możliwe, że trzeba dodać cat_picture do session_state, albo pozmieniać coś bardziej
    with cat_rest:
        if st.session_state['second_stage'] and cat_picture is not None:
            name = st.text_input('Your cat name', 'Rudy')
            age = st.slider('Your cat age', 0, 20, 1)
            st.write("More information about your cat:")
            st.write(name," to piękne imię dla kota!")
            st.write("Age: ", age)
            get_cat_to_dowland(cat_picture,name,age)
            with open("cat_picture.jpg","rb") as file:
                btn=st.download_button(
                    label="Download your cat",
                    data=file,
                    file_name='cat.jpg',
                    mime='image/jpg',)            


if __name__=="__main__":
    main()
    
