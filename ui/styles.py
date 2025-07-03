import streamlit as st

def inject_styles():
    st.markdown("""
    <style>
    .preview-card {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 18px;
        margin-bottom: 20px;
        background-color: #ffffff;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        transition: all 0.2s ease;
    }
    .preview-card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transform: translateY(-2px);
    }
    .preview-username {
        font-weight: 600;
        font-size: 1rem;
        color: #333;
        margin-bottom: 8px;
    }
    .preview-caption {
        font-size: 0.95rem;
        color: #111;
        line-height: 1.6;
    }
    .preview-footer {
        display: flex;
        justify-content: space-between;
        font-size: 0.8rem;
        color: #777;
        margin-top: 15px;
        padding-top: 10px;
        border-top: 1px solid #f0f0f0;
    }
    .stTextArea textarea {
        min-height: 250px !important;
        padding: 15px !important;
        line-height: 1.8 !important;
        font-size: 0.95rem !important;
    }
    .stButton>button {
        background-color: #4f46e5 !important;
        transition: all 0.2s !important;
    }
    .stButton>button:hover {
        background-color: #4338ca !important;
        transform: scale(1.02);
    }
    .section-header {
        padding-bottom: 8px;
        margin-bottom: 20px;
        border-bottom: 2px solid #f0f0f0;
    }
    .footer {
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #eee;
        text-align: center;
        color: #777;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)
