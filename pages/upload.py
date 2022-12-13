
import streamlit as st
import torch
from torchvision import transforms
from PIL import Image
import io
from matplotlib import pyplot as plt
import numpy as np

def load_model():
    run_model_path = './dirt.pt'
    model = torch.hub.load('ultralytics/yolov5','custom',path=run_model_path,force_reload=True)
    model.eval()
    return model

def load_image():
    uploaded_file = st.file_uploader(label='Pick an image to test')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        return Image.open(io.BytesIO(image_data))
    else:
        return None


def predict(model, image):
    print(type(image))
    output = model(image)
    return output

def main():
    model = load_model()
    image = load_image()
    result = predict(model,image)
    print(type(result))
    df = result.pandas().xyxy[0]
    print(df.to_dict('records'))
    print(df.to_dict('records')[0]['confidence'])
    st.image(np.squeeze(result.render()))


main()