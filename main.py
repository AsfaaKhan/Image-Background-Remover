import time
import streamlit as st
from rembg import remove 
from PIL import Image
from io import BytesIO

st.set_page_config(layout="wide",page_title="Image Background Remover", page_icon="📷" )


st.write("# 📸Image Background Remover📷")
st.markdown("\n")
st.markdown("\n")

st.write(
    "###### ✅ Try uploading an image to see the background magically removed! You can download the full-quality image from the sidebar. 🚀 "
)
st.markdown("\n")
st.markdown("\n")

st.sidebar.write("## Upload and Download Image 🔍")

MAX_FILE_SIZE = 5*1024*1024 #5MB

# Download the Fixed image
def covert_image(img):
    buffer = BytesIO()
    img.save(buffer,format="PNG")
    bytes_im = buffer.getvalue()
    return bytes_im


def fixed_image(upload):
    image= Image.open(upload)
    col1.write("##### Original Image 📷")
    col1.image(image)

    with col2:
        col2.write("##### Fixed Image 🔎 ")
        with st.spinner("Removing Background..."):
            time.sleep(5)
            fixed = remove(image)
        col2.image(fixed)
        st.sidebar.markdown("\n")
        st.sidebar.download_button("Download Fixed Image", covert_image(fixed), "fixed.png", "images/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=['.png', '.jpg','.jpeg'])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fixed_image(upload=my_upload)
else:    
    fixed_image("./image.png")
