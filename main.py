token_2 = 'your_token'

import streamlit as st
from openai import OpenAI
from PIL import Image
import base64
import io

client = OpenAI(api_key=token_2)

st.title("🎤 Voice → 🦁 Image Generator (Simple Version)")

st.write("Upload any audio file (it will not be used). I will just draw a lion image.")

# --- Audio Upload ---
audio_file = st.file_uploader("Upload audio file (.mp3, .wav, .m4a, .webm, .ogg)",
                              type=["mp3", "wav", "m4a", "webm", "ogg"])

if audio_file:
    st.audio(audio_file)
    st.success("Audio uploaded! (Not used in generation)")

    # --- Fixed Prompt ---
    st.subheader("🧠 Image Prompt (Fixed)")
    prompt_text = "A hyper-realistic, majestic lion standing on a rock at sunset"
    st.write(prompt_text)

    # --- Image Generation ---
    st.subheader("🎨 Generated Image")

    img_resp = client.images.generate(
        model="dall-e-3",
        prompt=prompt_text,
        size="1024x1024"
    )

    image_url = img_resp.data[0].url

    st.image(image_url, caption="Generated Image", use_column_width=True)



    # --- Logs ---
    st.subheader("📄 Logs")
    st.code(f"""
Audio used: NO
Prompt used: {prompt_text}
Image Model: dall-e-3
""")
