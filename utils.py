import re
import time
import random
import requests

from constants import (
    INTEL_PATTERNS,
    SCAM_SCORE_KEYWORDS,
    EARLY_QUESTIONS,
    LATE_QUESTIONS
)
from config import REPORTING_ENDPOINT

active_sessions = {}

def pick_unique(options, session):
    available = [r for r in options if r not in session["reply_history"]]
    return random.choice(available) if available else random.choice(options)

def scan_for_intel(text, session):
    clean_text = text.replace(",", " ").replace(";", " ").replace(":", " ")
    for cat, pattern in INTEL_PATTERNS.items():
        matches = re.findall(pattern, clean_text)
        for m in matches:
            m = m.rstrip(".,!?:;)")
            if m not in session["extractedIntelligence"][cat]:
                session["extractedIntelligence"][cat].append(m)

def update_risk_score(text, session):
    score = session["risk_score"]
    for word, weight in SCAM_SCORE_KEYWORDS.items():
        if word in text.lower():
            score += weight
    session["risk_score"] = score
    if score >= 20:
        session["is_scam"] = True

async def generate_persona_reply(turn, session):
    if turn == 1:
        return "Which branch are you calling from?"
    if turn == 2:
        return "I am ready to fix this, where should I click or send the details?"
    if turn == 3:
        return "What is the official website or portal link?"
    if turn == 4:
        return "Can you email me the instructions from your official email?"
    if turn == 5:
        return "Should I send money through UPI or bank transfer?"
    return pick_unique(LATE_QUESTIONS if turn >= 6 else EARLY_QUESTIONS, session)

def dispatch_final_report(session_id, session):
    duration = int(time.time() - session["startTime"])
    total_msgs = session["turns"] * 2

    payload = {
        "sessionId": session_id,
        "status": "success",
        "scamDetected": session["is_scam"],
        "totalMessagesExchanged": total_msgs,
        "extractedIntelligence": session["extractedIntelligence"],
        "engagementMetrics": {
            "engagementDurationSeconds": duration,
            "totalMessagesExchanged": total_msgs
        }
    }

    try:
        requests.post(REPORTING_ENDPOINT, json=payload, timeout=5)
    except:
        pass
