import os

_raw_keys = os.environ.get("GEMINI_KEY", "")
API_KEYS = [k.strip() for k in _raw_keys.split(",") if k.strip()]

API_KEY = os.environ.get("API_KEY")
REPORTING_ENDPOINT = "https://hackathon.guvi.in/api/updateHoneyPotFinalResult"
PORT = int(os.environ.get("PORT", 8000))
