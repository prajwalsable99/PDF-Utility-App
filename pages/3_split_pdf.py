import streamlit as st 
import PyPDF2 as pdf 

import io
from PyPDF2  import PdfReader,PdfWriter

def page_count(file):
    
    reader= PdfReader(file)
    count=len(reader.pages)

    

    return count
   
def split_pdf(file,x,y):

    reader= PdfReader(file)
    writer=PdfWriter()
    for  i in range(x-1,y):
        page= reader.pages[i]

        writer.add_page(page)

       
    pdf_buffer=io.BytesIO()
    writer.write(pdf_buffer)

    writer.close()
    pdf_buffer.seek(0)

    return pdf_buffer
    

st.set_page_config(page_title='PDF APP',page_icon='✅')
st.divider()

st.title('split Pdf')

uploaded_file = st.file_uploader("Upload pdf file to split /trim ",type=['pdf'],help='pdf',accept_multiple_files=False)

if uploaded_file != None:

    page_c=page_count(uploaded_file)

    try:
        st.markdown(f'## total pages : {page_c}')
        st.write('! pages starts from 1')
        x= st.number_input(' from page (inlcuded)', min_value=1,max_value=page_c-1)
        y= st.number_input('to page (included)',min_value=1,max_value=page_c)

        st.markdown(f'## trim : from :{x} to: {y}')

        if st.button('split'):
            if(x>y):
                st.error('enter valid range')
            else:
                st.write('success')
                try:
                    splitted_pdf=split_pdf(uploaded_file,x,y)
                    
                    st.download_button('download splitted pdf',splitted_pdf,'split.pdf','application/pdf')

                except Exception as e:
                    st.error(e)
    except Exception as e:
        st.error('file with 1 page not allowed')    

 




