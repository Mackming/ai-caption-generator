import streamlit as st

def inject_styles():
    st.markdown("""
    <style>
    /* ===== ULTRA PREMIUM CYBER THEME ===== */
    
    /* Global Reset */
    .stApp {
        background: #0A0A0F !important;
        color: #FFFFFF !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }
    
    /* Remove Streamlit Defaults */
    .main .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
    }
    
    /* ===== HERO SECTION - WOW FACTOR ===== */
    .premium-hero {
        background: linear-gradient(135deg, #0A0A0F 0%, #161622 50%, #0A0A0F 100%);
        padding: 5rem 2rem;
        text-align: center;
        position: relative;
        overflow: hidden;
        border-bottom: 1px solid #FF2E63;
        margin-bottom: 3rem;
    }
    
    .hero-glow {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(255, 46, 99, 0.15) 0%, transparent 70%);
        animation: pulse-glow 4s ease-in-out infinite;
    }
    
    @keyframes pulse-glow {
        0%, 100% { opacity: 0.5; transform: translate(-50%, -50%) scale(1); }
        50% { opacity: 0.8; transform: translate(-50%, -50%) scale(1.1); }
    }
    
    .hero-badge {
        display: inline-block;
        background: linear-gradient(135deg, #FF2E63, #FF6B9D);
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 25px;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 0 20px rgba(255, 46, 99, 0.3);
    }
    
    .hero-title {
        font-size: 5rem !important;
        font-weight: 900 !important;
        margin-bottom: 1rem !important;
        background: linear-gradient(135deg, #FFFFFF 0%, #FF2E63 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 30px rgba(255, 46, 99, 0.5);
    }
    
    .hero-gradient {
        background: linear-gradient(135deg, #FF2E63, #00D4FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: #94A3B8;
        margin-bottom: 3rem;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .text-cyber {
        background: linear-gradient(135deg, #FF2E63, #00D4FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }
    
    .hero-stats {
        display: flex;
        justify-content: center;
        gap: 3rem;
        margin-top: 2rem;
    }
    
    .stat {
        text-align: center;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #FF2E63, #00D4FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 0.5rem;
    }
    
    /* ===== PREMIUM CARDS ===== */
    .metric-card {
        background: rgba(22, 22, 34, 0.8);
        border: 1px solid #2D2D42;
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 46, 99, 0.1), transparent);
        transition: left 0.5s ease;
    }
    
    .metric-card:hover::before {
        left: 100%;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        border-color: #FF2E63;
        box-shadow: 0 10px 30px rgba(255, 46, 99, 0.2);
    }
    
    .metric-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #FFFFFF;
        margin-bottom: 0.25rem;
    }
    
    .metric-label {
        font-size: 0.8rem;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
    }
    
    /* ===== CYBER CARDS ===== */
    .preview-card {
        background: rgba(22, 22, 34, 0.9);
        border: 1px solid #2D2D42;
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .preview-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #FF2E63, #00D4FF);
    }
    
    .preview-card:hover {
        transform: translateY(-5px);
        border-color: #FF2E63;
        box-shadow: 0 15px 35px rgba(255, 46, 99, 0.2);
    }
    
    .preview-username {
        font-weight: 700;
        font-size: 1rem;
        color: #FFFFFF;
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .preview-caption {
        font-size: 0.95rem;
        color: #E2E8F0;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    .preview-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.8rem;
        color: #94A3B8;
        padding-top: 1rem;
        border-top: 1px solid #2D2D42;
    }
    
    .preview-platform {
        background: linear-gradient(135deg, #FF2E63, #00D4FF);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* ===== SUGGESTION CARDS ===== */
    .suggestion-card.cyber {
        background: rgba(22, 22, 34, 0.9);
        border: 1px solid #2D2D42;
        border-radius: 12px;
        padding: 1.25rem;
        display: flex;
        align-items: center;
        gap: 1rem;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .suggestion-card.cyber:hover {
        border-color: #FF2E63;
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(255, 46, 99, 0.2);
    }
    
    .suggestion-glow {
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 46, 99, 0.1), transparent);
        transition: left 0.5s ease;
    }
    
    .suggestion-card.cyber:hover .suggestion-glow {
        left: 100%;
    }
    
    .suggestion-icon {
        font-size: 1.5rem;
        background: linear-gradient(135deg, #FF2E63, #00D4FF);
        border-radius: 10px;
        width: 50px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }
    
    .suggestion-label {
        font-size: 0.8rem;
        color: #94A3B8;
        margin-bottom: 0.25rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 600;
    }
    
    .suggestion-value {
        font-size: 1rem;
        font-weight: 700;
        color: #FFFFFF;
    }
    
    /* ===== PREMIUM FORM ELEMENTS ===== */
    .input-section {
        background: rgba(22, 22, 34, 0.8);
        border: 1px solid #2D2D42;
        border-radius: 20px;
        padding: 2.5rem;
        margin: 2rem 0;
        backdrop-filter: blur(10px);
    }
    
    .section-header {
        text-align: center;
        margin-bottom: 2rem;
        padding-bottom: 1.5rem;
        border-bottom: 1px solid #2D2D42;
    }
    
    .section-header h2 {
        font-size: 2.5rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    .section-header p {
        color: #94A3B8;
        font-size: 1.1rem;
    }
    
    .results-header {
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .results-badge {
        display: inline-block;
        background: linear-gradient(135deg, #00D4FF, #FF2E63);
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 25px;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }
    
    .section-spacer {
        height: 2rem;
    }
    
    /* Form Elements */
    .stTextArea textarea {
        background: rgba(22, 22, 34, 0.8) !important;
        border: 1px solid #2D2D42 !important;
        border-radius: 12px !important;
        color: #FFFFFF !important;
        padding: 1rem !important;
        font-size: 1rem !important;
        line-height: 1.6 !important;
        min-height: 120px !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #FF2E63 !important;
        box-shadow: 0 0 0 2px rgba(255, 46, 99, 0.2) !important;
    }
    
    .stSelectbox div[data-baseweb="select"] {
        background: rgba(22, 22, 34, 0.8) !important;
        border: 1px solid #2D2D42 !important;
        border-radius: 12px !important;
        color: #FFFFFF !important;
    }
    
    .stSlider div[data-baseweb="slider"] {
        color: #FF2E63 !important;
    }
    
    .stCheckbox label {
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }
    
    /* ===== CYBER BUTTONS ===== */
    .stButton>button {
        background: linear-gradient(135deg, #FF2E63 0%, #FF6B9D 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 15px rgba(255, 46, 99, 0.3) !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(255, 46, 99, 0.4) !important;
        background: linear-gradient(135deg, #FF6B9D 0%, #FF2E63 100%) !important;
    }
    
    .stButton>button[kind="secondary"] {
        background: rgba(22, 22, 34, 0.8) !important;
        border: 1px solid #2D2D42 !important;
        color: #FFFFFF !important;
        box-shadow: none !important;
    }
    
    .stButton>button[kind="secondary"]:hover {
        border-color: #FF2E63 !important;
        background: rgba(255, 46, 99, 0.1) !important;
        transform: translateY(-2px) !important;
    }
    
    /* ===== PLATFORM TIP ===== */
    .platform-tip.cyber {
        background: rgba(255, 46, 99, 0.1);
        border: 1px solid #FF2E63;
        border-radius: 8px;
        padding: 0.75rem 1rem;
        margin: 0.5rem 0;
        color: #FF6B9D;
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    /* ===== EXPORT SECTION ===== */
    .export-section {
        background: rgba(22, 22, 34, 0.8);
        border: 1px solid #2D2D42;
        border-radius: 16px;
        padding: 2rem;
        margin: 2rem 0;
    }
    
    /* ===== RESPONSIVE DESIGN ===== */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 3rem !important;
        }
        
        .hero-stats {
            flex-direction: column;
            gap: 1.5rem;
        }
        
        .input-section {
            padding: 1.5rem;
        }
        
        .section-header h2 {
            font-size: 2rem !important;
        }
    }
    
    /* ===== SCROLLBAR ===== */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #161622;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #FF2E63;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #FF6B9D;
    }
    </style>
    """, unsafe_allow_html=True)
