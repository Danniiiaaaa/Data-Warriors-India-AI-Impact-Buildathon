import google.generativeai as genai
from config import API_KEYS

ai_model = None
CURRENT_KEY_INDEX = 0

def configure_ai():
    global ai_model, CURRENT_KEY_INDEX
    if not API_KEYS:
        return

    genai.configure(api_key=API_KEYS[CURRENT_KEY_INDEX])
    ai_model = genai.GenerativeModel(
        "gemini-1.5-flash",
        safety_settings=[
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ],
    )

def rotate_key():
    global CURRENT_KEY_INDEX
    if len(API_KEYS) <= 1:
        return False
    CURRENT_KEY_INDEX = (CURRENT_KEY_INDEX + 1) % len(API_KEYS)
    configure_ai()
    return True
