import streamlit as st 
import PyPDF2 as pdf 

import io
from PyPDF2  import PdfReader,PdfWriter



# page = reader.pages[0]
# count = 0

# for image_file_object in page.images:
#     with open(str(count) + image_file_object.name, "wb") as fp:
#         fp.write(image_file_object.data)
#         count += 1
    

def extractImages(uploaded_file):
    reader=PdfReader(uploaded_file)
    page_count=len(reader.pages)
    c=0

    for  i in range(0,page_count):
        page= reader.pages[i]
        for image_file_object in page.images:
            c=c+1
            st.write(f'{image_file_object.name}_{c}')

            image_buff=io.BytesIO(image_file_object.data)
            
            st.image(image_buff)
    if(c==0):
        st.error('no images found')

            



st.set_page_config(page_title='PDF APP',page_icon='✅')
st.divider()

st.title('Extract images from Pdf')

uploaded_file = st.file_uploader("Upload pdf file to extract image ",type=['pdf'],help='pdf',accept_multiple_files=False)

if uploaded_file != None:

    

    try:
       if(st.button('extract images')):
            extractImages(uploaded_file)
    except Exception as e:
        st.error(e)    

 




