import time
from fastapi import APIRouter, BackgroundTasks, Depends

from models import WebhookRequest
from security import verify_api_key
from utils import (
    active_sessions,
    scan_for_intel,
    update_risk_score,
    generate_persona_reply,
    dispatch_final_report
)

router = APIRouter()

@router.post("/api/honeypot", dependencies=[Depends(verify_api_key)])
async def handle_webhook(req: WebhookRequest, background_tasks: BackgroundTasks):
    sid = req.sessionId

    if sid not in active_sessions:
        active_sessions[sid] = {
            "is_scam": False,
            "turns": 0,
            "startTime": time.time(),
            "reply_history": [],
            "reported": False,
            "risk_score": 0,
            "extractedIntelligence": {
                "upiIds": [],
                "bankAccounts": [],
                "phishingLinks": [],
                "phoneNumbers": [],
                "emailAddresses": []
            }
        }

    session = active_sessions[sid]
    session["turns"] += 1
    text = req.message.text

    scan_for_intel(text, session)
    update_risk_score(text, session)

    reply = await generate_persona_reply(session["turns"], session)
    session["reply_history"].append(reply)

    if session["turns"] >= 9 and not session["reported"]:
        session["reported"] = True
        background_tasks.add_task(dispatch_final_report, sid, session)

    return {"status": "success", "reply": reply}
