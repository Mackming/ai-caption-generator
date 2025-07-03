import google.generativeai as genai
from google.api_core import exceptions
import streamlit as st

def generate_with_fallback(prompt, model_list, task_name="task"):
    for i, model_name in enumerate(model_list):
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(contents=[{"role": "user", "parts": [prompt]}])
            return response.text.strip(), model_name
        except exceptions.ResourceExhausted:
            if i < len(model_list) - 1:
                st.warning(f"⚠️ Rate limit reached for {model_name}. Switching to next model...")
            continue
        except Exception as e:
            if i < len(model_list) - 1:
                st.warning(f"⚠️ Error with {model_name}: {str(e)}. Trying next model...")
            continue
    raise exceptions.ResourceExhausted(f"All models failed for {task_name}")