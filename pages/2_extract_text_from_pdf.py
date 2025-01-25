import streamlit as st 
import PyPDF2 as pdf 
from PyPDF2  import PdfReader
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def summarize(text):
    text= text[:5000]
    try:
        # Use Groq's chat completions API for generating email content
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"summarize :{text}",
                }
            ],
            model="llama3-8b-8192",  # Choose an appropriate model
        )

        # Return the generated email
        return chat_completion.choices[0].message.content.strip()

    except Exception as e:
        return f"Unable to connect at the moment"


def read_pdf(file):
    reader= PdfReader(file)
    page_count=len(reader.pages)

    text=''
    for  i in range(0,page_count):
        page_text= reader.pages[i].extract_text()
        text+= page_text +'\n'
    
    return text


st.set_page_config(page_title='PDF APP',page_icon='✅')

st.divider()
st.title('Extract Text from Pdf')

uploaded_file = st.file_uploader("Upload a pdf file",type=['pdf'],help='pdf',accept_multiple_files=False)

if uploaded_file !=None:
    


    pdf_data=read_pdf(uploaded_file)
   

    c1,c2=st.columns(2)

    with c1:
        st.markdown('## Extracted Text : ')
        st.markdown(f'<div style= "height:600px;overflow-y:scroll ;border : 1px solid gray;padding: 4px" > {pdf_data}</div> ',unsafe_allow_html=True)
    with c2:
        st.markdown('## Summarized Text : ')

        st.markdown(f'``` {summarize(pdf_data)}```')



