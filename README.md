# AI Caption Generator

An advanced AI-powered tool built with Streamlit to generate engaging social media captions customized by tone, platform, persona, and language. Powered by Google Gemini Pro models.

---

FEATURES

- Tailored caption generation (tone, persona, platform)
- Emoji and hashtag toggles
- AI-powered tone & persona suggestions
- Export captions as .txt, .csv, or .json
- Supports English, Urdu, Arabic, French, and Spanish
- Clean, modern, responsive UI

---

INSTALLATION

1. Clone the repository:

   git clone https://github.com/Mackming/ai-caption-generator.git
   cd ai-caption-generator

2. Install dependencies:

   pip install -r requirements.txt

3. Set up environment variables:

   Copy the example file:
   cp .env.example .env

   Then add your Google Gemini API key to `.env`:

   GOOGLE_API_KEY=your-gemini-api-key-here

4. Run the application:

   streamlit run app.py

---

DEPLOYMENT

Deploy to Streamlit Cloud by pushing this repo to GitHub.

IMPORTANT: Set GOOGLE_API_KEY as a Secret Environment Variable in Streamlit Cloud:  
https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/set-up-secrets

---

ENVIRONMENT VARIABLES

Create a `.env` file with the following:

   GOOGLE_API_KEY=your-gemini-api-key-here

Get your Gemini API key from:  
https://makersuite.google.com/app/apikey

WARNING: Do NOT commit your `.env` file to GitHub.  
Use `.env.example` to guide others in setting up the project safely.

---

CREDITS

Built with ❤️ by:
Taqi Kazmi — https://instagram.com/taqikvzmi  
Ali Jamal — https://instagram.com/alijamalashraf
