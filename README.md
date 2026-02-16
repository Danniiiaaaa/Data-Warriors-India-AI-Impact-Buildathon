# Data-Warriors-India-AI-Impact-Buildathon
grand finale

Here is a **clean, judge-friendly README.md** you can paste directly into your repo.

---

# 🛡️ AI Honeypot Scam Detection API

## Overview

This project is an AI-powered honeypot API designed to **detect scam conversations, engage scammers, and extract actionable intelligence** such as phone numbers, UPI IDs, phishing links, bank accounts, and email addresses.

The system simulates a realistic victim persona and keeps scammers engaged in multi-turn conversations while safely collecting fraud infrastructure data.

The goal is to **waste scammer time and gather intelligence** in a safe and automated way.

---

# 🎯 Key Features

### Scam Detection

* Keyword-based risk scoring system
* Multi-scenario support (bank fraud, UPI fraud, phishing, investment scams, etc.)
* Generic detection logic (no hardcoded scenarios)

### Intelligence Extraction

Automatically extracts:

* 📞 Phone numbers
* 🏦 Bank account numbers
* 💳 UPI IDs
* 🔗 Phishing URLs
* 📧 Email addresses

Regex extraction is fully generic and works for unseen scam data.

---

### Multi-Turn Honeypot Engagement

The honeypot follows a **progressive bait strategy**:

| Conversation Stage | Goal                                  |
| ------------------ | ------------------------------------- |
| Early turns        | Ask for portal, email, payment method |
| Mid turns          | Force UPI and phone disclosure        |
| Late turns         | Harvest secondary infrastructure      |

Late-stage intelligence harvesting:

* Backup phone number
* Alternate UPI ID
* WhatsApp support number
* Secondary phishing links
* Additional email contacts
* Senior officer escalation

This creates **realistic victim behaviour** and maximizes intelligence extraction.

---

# 🧠 Architecture

```
Scammer Message → Risk Scoring → Intelligence Extraction
                         ↓
                Persona Reply Engine
                         ↓
           Multi-Turn Engagement Strategy
                         ↓
              Final Intelligence Report
```

### Components

| Module            | Purpose                                    |
| ----------------- | ------------------------------------------ |
| Risk Scoring      | Detect scam intent using weighted keywords |
| Entity Extraction | Regex-based intelligence collection        |
| Persona Engine    | Generates victim-like responses            |
| Session Manager   | Tracks conversation state                  |
| Report Dispatcher | Sends final structured output              |

---

# 🧰 Tech Stack

* **Python**
* **FastAPI** – API framework
* **Uvicorn** – ASGI server
* **Google Gemini API** – LLM integration (optional fallback)
* **Regex/NLP** – Intelligence extraction

---

# 🚀 Setup Instructions

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/honeypot-api
cd honeypot-api
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Create environment file

Create `.env` file:

```
GEMINI_KEY=your_gemini_api_key_optional
PORT=8000
```

## 4. Run the API

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

# 🌐 API Endpoint

### POST `/api/honeypot`

#### Request

```json
{
  "sessionId": "uuid",
  "message": {
    "sender": "scammer",
    "text": "Your account is blocked. Send OTP now."
  },
  "conversationHistory": [],
  "metadata": {
    "channel": "SMS",
    "language": "English",
    "locale": "IN"
  }
}
```

#### Response

```json
{
  "status": "success",
  "reply": "Which branch are you calling from?"
}
```

---

# 📤 Final Output Submission

After conversation completion, the API automatically sends:

```json
{
  "sessionId": "session-id",
  "status": "success",
  "scamDetected": true,
  "totalMessagesExchanged": 18,
  "extractedIntelligence": {
    "phoneNumbers": [],
    "bankAccounts": [],
    "upiIds": [],
    "phishingLinks": [],
    "emailAddresses": []
  },
  "engagementMetrics": {
    "engagementDurationSeconds": 120,
    "totalMessagesExchanged": 18
  },
  "agentNotes": "Collected scam infrastructure details."
}
```

---

# 🔍 Approach

## Scam Detection Strategy

* Weighted keyword scoring system
* Generic fraud pattern detection
* Works across multiple scam types

## Intelligence Extraction Strategy

* Regex-based entity detection
* Multi-pass extraction with cleanup
* Punctuation and formatting normalization

## Engagement Strategy

* Realistic victim persona
* Multi-stage baiting
* Infrastructure harvesting
* Long conversation maintenance

---

# 🔒 Security & Ethics

This project is designed for **defensive cybersecurity research** and **fraud prevention**.
No real credentials are shared or requested.

---

# 📌 Summary

This honeypot:

* Detects scams generically
* Extracts actionable intelligence
* Maintains realistic engagement
* Produces structured fraud reports

Built to simulate real-world honeypot behaviour at scale.

---

If you want, I can also give a short `architecture.md` for extra polish.

