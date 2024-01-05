
import numpy as np


import streamlit as st
import io
from PIL import Image



st.set_page_config(
    page_title="<Your Name> Portfolio",
    page_icon="📊",
)



with st.sidebar:
    st.image("eae_img.png", width=200)
    st.write("Interactive Project to open, crop, display and save images using NumPy, PIL and Matplotlib.")



st.title("🖼️ Image Cropper")
st.divider()



is_example = False
img = st.file_uploader("Upload an image:", type=["png", "jpg", "jpeg"])

if img is None:
    is_example = True
    with Image.open("data/starry_night.png") as img:
        img_arr = np.array(img)
else:
    with Image.open(img) as img:
        img_arr = np.array(img)


st.image(img_arr, caption="Original Image" if not is_example else "Original example image", use_column_width=True)
st.write("#")




min_height = 0 
max_height = img_arr.shape[0]   

min_width = 0
max_width = img_arr.shape[1]    



if type(max_height) == int and type(max_width) == int:
    
    cols1 = st.columns([4, 1, 4])

    
    crop_min_h, crop_max_h = cols1[0].slider("Crop Vertical Range", min_height, max_height, (int(max_height*0.1), int(max_height*0.9)))   
    
    crop_min_w, crop_max_w = cols1[2].slider("Crop Horizontal Range", min_width, max_width, (int(max_width*0.1), int(max_width*0.9)))    


    st.write("## Cropped Image")

else:
    st.subheader("⚠️ You still need to develop the Ex 1.1.")




crop_arr = np.array(img_arr[crop_min_h:crop_max_h,crop_min_w:crop_max_w])  




if type(crop_arr) == np.ndarray:
    st.image(crop_arr, caption="Cropped Image", use_column_width=True)

    buf = io.BytesIO()
    Image.fromarray(crop_arr).save(buf, format="PNG")
    cropped_img_bytes = buf.getvalue()

    cols2 = st.columns([4, 1, 4])
    file_name = cols2[0].text_input("Chose a File Name:", "cropped_image") + ".png"

    st.download_button(f"Download the image `{file_name}`", cropped_img_bytes, file_name=file_name)

else:
    st.subheader("⚠️ You still need to develop the Ex 1.3.")
