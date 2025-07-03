import streamlit as st
from config.constants import TONE_OPTIONS, PERSONA_OPTIONS, PLATFORM_INFO, SUGGESTION_MODELS, CAPTION_MODELS
from core.generator import generate_with_fallback
from core.sanitizer import sanitize_input
from core.parser import parse_captions
from ui.styles import inject_styles
from ui.components import render_preview, render_footer
from utils.export import generate_downloads
import re
import json
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


st.set_page_config(page_title="AI Caption Generator", layout="centered")
st.title("📝 AI Caption Generator")
inject_styles()

# Session state
st.session_state.setdefault("auto_selected_tone", "Professional")
st.session_state.setdefault("auto_selected_persona", "None")
st.session_state.setdefault("captions_generated", False)
st.session_state.setdefault("captions", [])
st.session_state.setdefault("form_data", {
    "product_desc": "",
    "tone": "Professional",
    "persona": "None",
    "platform": "Instagram",
    "caption_count": 5,
    "use_emojis": True,
    "use_hashtags": False,
    "language": "English"
})

# Output view
if st.session_state["captions_generated"]:
    st.markdown("### ✨ Generated Captions")
    for i, caption in enumerate(st.session_state["captions"]):
        render_preview(caption, st.session_state.get("platform", "Instagram"), i)

    st.markdown("---")
    st.markdown("### 📋 Copy All Captions")
    formatted_captions = "\n\n".join(st.session_state["captions"])
    st.text_area("Copy the captions below:", value=formatted_captions, height=300, label_visibility="collapsed")

    txt_data, csv_data, json_data = generate_downloads(
        st.session_state["captions"],
        {
            "platform": st.session_state["platform"],
            "tone": st.session_state["tone"],
            "persona": st.session_state["persona"]
        }
    )
    st.markdown("---")
    st.markdown("### 💾 Export Options")

    filename = st.text_input("**Filename**", "captions")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.download_button("Text (.txt)", txt_data, f"{filename}.txt", "text/plain", use_container_width=True)
    with col2:
        st.download_button("CSV (.csv)", csv_data, f"{filename}.csv", "text/csv", use_container_width=True)
    with col3:
        st.download_button("JSON (.json)", json_data, f"{filename}.json", "application/json", use_container_width=True)

    st.markdown("---")
    if st.button("🔄 Generate New Set", use_container_width=True):
        st.session_state["captions_generated"] = False
        st.session_state["captions"] = []
        st.rerun()

# Input view
else:
    st.markdown("### 🧠 Input Parameters")
    MIN_DESC_LEN = 15
    form_data = st.session_state.form_data

    product_desc = st.text_area("**Product/Service Description (Required)**", 
        value=form_data["product_desc"], height=140, max_chars=300,
        placeholder="Describe your product/service...\ne.g. Premium leather gloves designed for winter in Canada", key="product_desc_input")

    suggestions_container = st.empty()

    if st.button("🎯 Suggest Tones & Persona", use_container_width=True):
        if not product_desc or len(product_desc.strip()) < MIN_DESC_LEN:
            st.warning(f"Product description must be at least {MIN_DESC_LEN} characters.")
        else:
            with st.spinner("Analyzing product..."):
                try:
                    tone_prompt = f"""
Analyze the product and return JSON with:
{{
    "tone": "best_matching_tone_from_list",
    "persona": "suitable_persona_from_list"
}}
Available tones: {', '.join(TONE_OPTIONS)}
Available personas: {', '.join(PERSONA_OPTIONS[1:])}
Product: {product_desc}
"""
                    raw_json_text, model_used = generate_with_fallback(tone_prompt, SUGGESTION_MODELS)
                    json_match = re.search(r'\{.*\}', raw_json_text, re.DOTALL)

                    tone, persona = "", ""
                    if json_match:
                        try:
                            data = json.loads(json_match.group())
                            tone = data.get("tone", "")
                            persona = data.get("persona", "")
                        except:
                            pass

                    if tone:
                        st.session_state["auto_selected_tone"] = tone
                    if persona:
                        st.session_state["auto_selected_persona"] = persona

                    if tone or persona:
                        with suggestions_container.container():
                            st.markdown("### AI Suggestions")
                            st.caption(f"Used model: {model_used.split('/')[-1]}")
                            if tone:
                                st.markdown(f"""
                                <div class="preview-card" style="padding:12px; margin-bottom:10px;">
                                    <div style="display:flex; align-items:center;">
                                        <div style="background-color:#f0f2f6; border-radius:50%; width:32px; height:32px; display:flex; align-items:center; justify-content:center; margin-right:12px;">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#4f46e5" viewBox="0 0 16 16">
                                                <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2z"/>
                                            </svg>
                                        </div>
                                        <div>
                                            <div style="font-size:0.9rem; color:#666;">Suggested Tone</div>
                                            <div style="font-weight:600; color:#333;">{tone}</div>
                                        </div>
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)

                            if persona:
                                st.markdown(f"""
                                <div class="preview-card" style="padding:12px;">
                                    <div style="display:flex; align-items:center;">
                                        <div style="background-color:#f0f2f6; border-radius:50%; width:32px; height:32px; display:flex; align-items:center; justify-content:center; margin-right:12px;">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#4f46e5" viewBox="0 0 16 16">
                                                <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2z"/>
                                            </svg>
                                        </div>
                                        <div>
                                            <div style="font-size:0.9rem; color:#666;">Suggested Persona</div>
                                            <div style="font-weight:600; color:#333;">{persona}</div>
                                        </div>
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)

                except Exception as e:
                    st.warning("Could not generate suggestions.")
                    st.expander("Error Details").write(str(e))

    with st.form(key="input_form"):
        col1, col2 = st.columns(2)
        with col1:
            tone = st.selectbox("**Tone / Style (Required)**", TONE_OPTIONS,
                                index=TONE_OPTIONS.index(st.session_state["auto_selected_tone"]))
        with col2:
            persona = st.selectbox("**Persona / Voice Style**", PERSONA_OPTIONS,
                                   index=PERSONA_OPTIONS.index(st.session_state["auto_selected_persona"]))

        platform = st.selectbox("**Social Media Platform (Required)**", list(PLATFORM_INFO.keys()), 
                                index=list(PLATFORM_INFO.keys()).index(form_data["platform"]))
        st.caption(f"💡 {PLATFORM_INFO[platform]}")
        caption_count = st.slider("**Number of Captions**", 1, 10, value=form_data["caption_count"])
        col1, col2 = st.columns(2)
        with col1:
            use_emojis = st.checkbox("**Add Emojis**", value=form_data["use_emojis"])
        with col2:
            use_hashtags = st.checkbox("**Add Hashtags**", value=form_data["use_hashtags"])

        language = st.selectbox("**Output Language (Required)**", ["English", "Urdu", "Arabic", "French", "Spanish"], 
                                index=["English", "Urdu", "Arabic", "French", "Spanish"].index(form_data["language"]))
        submit = st.form_submit_button("✨ Generate Captions", use_container_width=True)

    if submit:
        suggestions_container.empty()
        if not product_desc or len(product_desc.strip()) < MIN_DESC_LEN:
            st.error(f"🚫 Product description is required and must be at least {MIN_DESC_LEN} characters.")
        elif re.search(r'[^\w\s.,!?@#$%^&*()-+=/\'\"<>]', product_desc):
            st.error("❌ Invalid characters in description")
        else:
            st.session_state.form_data = {
                "product_desc": product_desc,
                "tone": tone,
                "persona": persona,
                "platform": platform,
                "caption_count": caption_count,
                "use_emojis": use_emojis,
                "use_hashtags": use_hashtags,
                "language": language
            }
            with st.status("✨ Generating captions with AI...", expanded=True) as status:
                try:
                    st.write("🔒 Sanitizing input...")
                    safe_product_desc = sanitize_input(product_desc.strip())

                    st.write("🧠 Building prompt...")
                    persona_text = persona if persona != "None" else ""
                    prompt = f"""
You are a professional social media copywriter.

Generate {caption_count} unique captions for a marketing post.

Product/service: {safe_product_desc}
Platform: {platform}
Tone/style: {tone}
Language: {language}
Persona/voice: {persona_text}
Include emojis: {use_emojis}
Include hashtags: {use_hashtags}

Guidelines:
- Make each caption unique and engaging
- Match the tone and platform audience
- Be concise and impactful
- If emojis are selected, include relevant emojis
- If hashtags are selected, include relevant hashtags
- Return only the final captions, no extra commentary
- Write all captions in {language}
- Number each caption like `1.` or `1)` on a new line
"""

                    st.write("🚀 Generating content...")
                    captions_raw, model_used = generate_with_fallback(prompt, CAPTION_MODELS)
                    st.write(f"🧠 Using model: {model_used.split('/')[-1]}")
                    st.write("🧹 Cleaning results...")
                    captions = parse_captions(captions_raw, caption_count)

                    cleaned_captions = []
                    for caption in captions:
                        if not use_hashtags:
                            caption = re.sub(r'\s*#\w+', '', caption).strip()
                        cleaned_captions.append(caption)

                    st.session_state["captions"] = cleaned_captions
                    st.session_state["captions_generated"] = True
                    st.session_state["platform"] = platform
                    st.session_state["tone"] = tone
                    st.session_state["persona"] = persona

                    status.update(label="✅ Captions generated successfully!", state="complete")
                    st.rerun()
                except Exception as e:
                    status.update(label="❌ Generation failed", state="error")
                    st.error("Something went wrong while generating captions.")
                    st.expander("Error Details").write(str(e))

render_footer()