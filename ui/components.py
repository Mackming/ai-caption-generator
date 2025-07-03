import streamlit as st

def render_preview(caption, platform, index, username="@yourbrand"):
    st.markdown(f"""
    <div class=\"preview-card\">
        <div class=\"preview-username\">{username}</div>
        <div class=\"preview-caption\">{caption}</div>
        <div class=\"preview-footer\">#{platform.lower()} • Post {index+1} • {len(caption)} characters</div>
    </div>
    """, unsafe_allow_html=True)

def render_footer():
    st.markdown("""
    <div class=\"footer\">
        Built with ❤️ by <a href=\"https://instagram.com/taqikvzmi\" target=\"_blank\">Taqi Kazmi</a> and <a href=\"https://instagram.com/alijamalashraf\" target=\"_blank\">Ali Jamal</a>
    </div>
    """, unsafe_allow_html=True)