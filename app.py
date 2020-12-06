import streamlit as st
from PIL import Image
from clf import predict
import streamlit.components.v1 as components
import ht
st.set_page_config(layout='wide',initial_sidebar_state='collapsed')
st.set_option('deprecation.showfileUploaderEncoding', False)
components.html(ht.header2,height=150,width=1500)
st.title(" Simple Image Classification App Using Deep Learning")
st.write("Upload the Image Below and See the predicted objects name along with their porbability score")

file_up = st.file_uploader("Upload an image", type="jpg")

if file_up is not None:
    image = Image.open(file_up)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Just a second...")
    labels = predict(file_up)

    # print out the top 5 prediction labels with scores
    for i in labels:
        st.write("Prediction (index, name)", i[0], ",   Score: ", i[1])