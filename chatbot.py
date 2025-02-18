import streamlit as st
from PyPDF2 import PdfFileReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
#Upload pdf file
st.header("ChatBot of Manh")
with st.sidebar :
    st.title('Your documents')
    file = st.file_uploader("Upload a PDF file and start asking questions", type="pdf")
#Extract the text
if file not None :
    pdf_reader = PdfFileReader(file)
    text = ''
    for page in  pdf_reader.pages:
        text += page.extract_text()
        #st.write(text)

#Break it into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators = "\n",
        chunk_size = 1000,
        chunk_overlap = 150,
        leght_funtion = len
    )
    chunks  = text_splitter.split_text(text)
    st.write(chunks)