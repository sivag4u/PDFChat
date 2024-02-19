import requests
from langchain_community.llms import OpenAI
import streamlit as st
import os 
open_api_key="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"
os.environ["OPENAI_API_KEY"]=open_api_key

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}



##initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": input,
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.image(image)

#image.show()