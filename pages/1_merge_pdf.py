import streamlit as st 
import PyPDF2 as pdf 
from PyPDF2  import PdfMerger
import io


def merge_pdf(uploaded_files):
    merger=PdfMerger()
    

    for uploaded_file in uploaded_files:
        merger.append(uploaded_file)

        # merger.write(f)
    pdf_buffer=io.BytesIO()
    merger.write(pdf_buffer)

    merger.close()
    pdf_buffer.seek(0)

    return pdf_buffer
   


st.set_page_config(page_title='PDF APP',page_icon='✅')
st.divider()

st.title('Merge Pdf')

uploaded_files = st.file_uploader("Upload all pdf files to merge",type=['pdf'],help='pdf',accept_multiple_files=True)

if len(uploaded_files)!=0:

    button=st.button('merge')
    if(button):
        try:
            final=merge_pdf(uploaded_files)
            st.download_button('download merged pdf',final,'merged.pdf','application/pdf')

        except Exception as e:
            st.error(e)
    else:
        st.error('downlaod the pdf after merging')

 




