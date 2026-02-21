INTEL_PATTERNS = {
    "upiIds": r"\b[a-zA-Z0-9.\-_]{2,256}@[a-zA-Z]{2,64}\b(?!\.)",
    "bankAccounts": r"\b\d{11,18}\b",
    "phishingLinks": r"(https?://[^\s]+|bit\.ly/[^\s]+|tinyurl\.com/[^\s]+|[a-zA-Z0-9\-]+\.(?:com|in|co)/[^\s]*)",
    "phoneNumbers": r"(?<!\d)(?:\+91[\-\s]?)?[6-9]\d{9}\b",
    "emailAddresses": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
}

SCAM_SCORE_KEYWORDS = {
    "otp": 30, "pin": 30, "upi": 25, "kyc": 15,
    "blocked": 15, "urgent": 10, "verify": 10,
    "http": 20, "https": 20, "link": 15,
    "offer": 10, "deal": 10, "gift": 15,
    "prize": 15, "refund": 15, "cashback": 15
}

EARLY_QUESTIONS = [
    "Which department are you calling from?",
    "What is your official callback number?",
    "Which branch are you calling from?",
    "Can you verify your identity first?",
    "I received an OTP screen, where do I enter it?"
]

LATE_QUESTIONS = [
    "Do you have a backup number in case this line disconnects?",
    "Is there another UPI ID in case this one fails?",
    "Can you send the link again from your main website?",
    "Do you have a WhatsApp number for support?",
    "Can your senior officer contact me directly?",
    "Is there another email I can CC for confirmation?"
]
