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
import time

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# =============================
# 🚀 PREMIUM PAGE CONFIG
# =============================
st.set_page_config(
    page_title="CAPTION AI | Next-Gen Content Creation",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🚀"
)

# =============================
# 🎨 INJECT ULTRA PREMIUM STYLES
# =============================
inject_styles()

# =============================
# 🌟 HERO SECTION - WOW FACTOR
# =============================
st.markdown("""
<div class="premium-hero">
    <div class="hero-glow"></div>
    <div class="hero-content">
        <div class="hero-badge">🚀 NEXT-GEN AI</div>
        <h1 class="hero-title">CAPTION <span class="hero-gradient">AI</span></h1>
        <p class="hero-subtitle">Transform ordinary descriptions into <span class="text-cyber">VIRAL</span> social media content with cutting-edge AI</p>
        <div class="hero-stats">
            <div class="stat">
                <div class="stat-number">10x</div>
                <div class="stat-label">Engagement Boost</div>
            </div>
            <div class="stat">
                <div class="stat-number">50+</div>
                <div class="stat-label">Platform Styles</div>
            </div>
            <div class="stat">
                <div class="stat-number">0.5s</div>
                <div class="stat-label">Generation Speed</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =============================
# 🔄 SESSION STATE
# =============================
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

# =============================
# 🎯 MAIN CONTENT AREA
# =============================
if st.session_state["captions_generated"]:
    # RESULTS VIEW - PREMIUM LAYOUT
    st.markdown("""
    <div class="results-header">
        <div class="results-badge">✨ GENERATION COMPLETE</div>
        <h2>Your <span class="text-cyber">AI-Powered</span> Captions</h2>
    </div>
    """, unsafe_allow_html=True)

    # Performance Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon">📊</div>
            <div class="metric-value">{len(st.session_state["captions"])}</div>
            <div class="metric-label">CAPTIONS</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon">🎯</div>
            <div class="metric-value">{st.session_state.get("platform", "IG")}</div>
            <div class="metric-label">PLATFORM</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon">⚡</div>
            <div class="metric-value">{st.session_state.get("tone", "PRO")}</div>
            <div class="metric-label">TONE</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon">🚀</div>
            <div class="metric-value">AI</div>
            <div class="metric-label">POWERED</div>
        </div>
        """, unsafe_allow_html=True)

    # Captions Grid
    st.markdown("<div class='section-spacer'></div>", unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, caption in enumerate(st.session_state["captions"]):
        with cols[i % 2]:
            render_preview(caption, st.session_state.get("platform", "Instagram"), i)

    # Export Section
    st.markdown("""
    <div class="export-section">
        <div class="section-header">
            <h3>📦 <span class="text-cyber">EXPORT</span> YOUR CONTENT</h3>
            <p>Download in multiple formats for seamless workflow integration</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("#### 📋 Copy All Captions")
        formatted_captions = "\n\n".join(st.session_state["captions"])
        st.text_area("", value=formatted_captions, height=200, label_visibility="collapsed")

    with col2:
        st.markdown("#### 💾 Export Formats")
        filename = st.text_input("**Filename**", "ai_captions", label_visibility="collapsed")
        
        txt_data, csv_data, json_data = generate_downloads(
            st.session_state["captions"],
            {
                "platform": st.session_state["platform"],
                "tone": st.session_state["tone"],
                "persona": st.session_state["persona"]
            }
        )
        
        st.download_button("📄 TEXT FILE", txt_data, f"{filename}.txt", "text/plain", use_container_width=True)
        st.download_button("📊 CSV DATA", csv_data, f"{filename}.csv", "text/csv", use_container_width=True)
        st.download_button("🔷 JSON EXPORT", json_data, f"{filename}.json", "application/json", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # New Generation CTA
    st.markdown("<div class='section-spacer'></div>", unsafe_allow_html=True)
    if st.button("🚀 GENERATE NEW SET", use_container_width=True, type="primary"):
        st.session_state["captions_generated"] = False
        st.session_state["captions"] = []
        st.rerun()

else:
    # INPUT VIEW - PREMIUM FORM
    st.markdown("""
    <div class="input-section">
        <div class="section-header">
            <h2>🎨 <span class="text-cyber">CREATE</span> CAPTIONS</h2>
            <p>Describe your product and let AI work its magic</p>
        </div>
    """, unsafe_allow_html=True)

    MIN_DESC_LEN = 15
    form_data = st.session_state.form_data

    # Product Description with Premium Styling
    st.markdown("#### 📝 PRODUCT DESCRIPTION")
    product_desc = st.text_area(
        "", 
        value=form_data["product_desc"], 
        height=140,
        max_chars=300,
        placeholder="🚀 Describe your product/service in detail...\n\n💡 Example: Premium eco-friendly water bottles with smart temperature control and built-in hydration tracking",
        key="product_desc_input",
        label_visibility="collapsed"
    )

    # AI Suggestions
    suggestions_container = st.empty()

    if st.button("🤖 AI SUGGESTIONS: AUTO-DETECT STYLE", use_container_width=True, type="secondary"):
        if not product_desc or len(product_desc.strip()) < MIN_DESC_LEN:
            st.warning(f"📝 Description must be at least {MIN_DESC_LEN} characters for AI analysis.")
        else:
            with st.spinner("🔮 AI is analyzing your content..."):
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
                            st.markdown("#### 🤖 AI RECOMMENDATIONS")
                            st.caption(f"Powered by: {model_used.split('/')[-1]}")
                            
                            sug_col1, sug_col2 = st.columns(2)
                            with sug_col1:
                                if tone:
                                    st.markdown(f"""
                                    <div class="suggestion-card cyber">
                                        <div class="suggestion-icon">🎭</div>
                                        <div class="suggestion-content">
                                            <div class="suggestion-label">OPTIMAL TONE</div>
                                            <div class="suggestion-value">{tone}</div>
                                        </div>
                                        <div class="suggestion-glow"></div>
                                    </div>
                                    """, unsafe_allow_html=True)
                            
                            with sug_col2:
                                if persona:
                                    st.markdown(f"""
                                    <div class="suggestion-card cyber">
                                        <div class="suggestion-icon">👤</div>
                                        <div class="suggestion-content">
                                            <div class="suggestion-label">BEST PERSONA</div>
                                            <div class="suggestion-value">{persona}</div>
                                        </div>
                                        <div class="suggestion-glow"></div>
                                    </div>
                                    """, unsafe_allow_html=True)

                except Exception as e:
                    st.warning("⚠️ AI suggestions temporarily unavailable.")
                    st.expander("Technical Details").write(str(e))

    # Main Form
    with st.form(key="premium_input_form"):
        st.markdown("#### ⚙️ CONTENT CONFIGURATION")
        
        col1, col2 = st.columns(2)
        with col1:
            tone = st.selectbox("**TONE STYLE** 🎭", TONE_OPTIONS,
                                index=TONE_OPTIONS.index(st.session_state["auto_selected_tone"]))
        with col2:
            persona = st.selectbox("**VOICE PERSONA** 👤", PERSONA_OPTIONS,
                                   index=PERSONA_OPTIONS.index(st.session_state["auto_selected_persona"]))

        platform = st.selectbox("**SOCIAL PLATFORM** 📱", list(PLATFORM_INFO.keys()), 
                                index=list(PLATFORM_INFO.keys()).index(form_data["platform"]))
        st.markdown(f'<div class="platform-tip cyber">💡 {PLATFORM_INFO[platform]}</div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            caption_count = st.slider("**CAPTION COUNT** 🔢", 1, 10, value=form_data["caption_count"])
        with col2:
            use_emojis = st.checkbox("**ADD EMOJIS** 😊", value=form_data["use_emojis"])
        with col3:
            use_hashtags = st.checkbox("**ADD HASHTAGS** #️⃣", value=form_data["use_hashtags"])

        language = st.selectbox("**OUTPUT LANGUAGE** 🌍", ["English", "Urdu", "Arabic", "French", "Spanish"], 
                                index=["English", "Urdu", "Arabic", "French", "Spanish"].index(form_data["language"]))
        
        # Generate Button
        submit_col1, submit_col2, submit_col3 = st.columns([1, 2, 1])
        with submit_col2:
            submit = st.form_submit_button("🚀 GENERATE CAPTIONS", use_container_width=True, type="primary")

    st.markdown("</div>", unsafe_allow_html=True)

    if submit:
        suggestions_container.empty()
        if not product_desc or len(product_desc.strip()) < MIN_DESC_LEN:
            st.error(f"🚫 Description must be at least {MIN_DESC_LEN} characters.")
        elif re.search(r'[^\w\s.,!?@#$%^&*()-+=/\'\"<>]', product_desc):
            st.error("❌ Invalid characters detected")
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
            
            # Premium Generation Process
            with st.status("🚀 **AI GENERATION INITIATED**", expanded=True) as status:
                steps = [
                        ("🔒 INPUT SANITIZATION", 10),
                        ("🧠 AI PROMPT ENGINEERING", 25),
                        ("⚡ NEURAL PROCESSING", 50),
                        ("🎨 CONTENT ENHANCEMENT", 75),
                        ("✨ FINAL OPTIMIZATION", 90)
                    ]
                
                progress_bar = st.progress(0)
                
                try:
                    for step_text, progress in steps:
                        status.write(f"**{step_text}**")
                        safe_product_desc = sanitize_input(product_desc.strip())
                        progress_bar.progress(progress)
                        time.sleep(0.3)  # Visual effect only
                    
                    # Actual AI Processing
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
                    captions_raw, model_used = generate_with_fallback(prompt, CAPTION_MODELS)
                    status.write(f"🧠 **AI MODEL:** {model_used.split('/')[-1]}")
                    
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

                    progress_bar.progress(100)
                    status.update(label="✅ **GENERATION SUCCESSFUL!**", state="complete")
                    st.balloons()
                    st.rerun()
                    
                except Exception as e:
                    progress_bar.empty()
                    status.update(label="❌ **GENERATION FAILED**", state="error")
                    st.error("AI processing error occurred.")
                    st.expander("Technical Details").write(str(e))

# =============================
# 👣 PREMIUM FOOTER
# =============================
render_footer()
