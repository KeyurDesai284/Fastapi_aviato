from fastapi import APIRouter, HTTPException
import smtplib
from email.mime.text import MIMEText

router = APIRouter()

@router.post("/send_invite")
def send_invite():
    msg = MIMEText("Check the API documentation at: http://127.0.0.1:8000/redoc")
    msg['Subject'] = 'API Documentation Invitation'
    msg['From'] = 'sender_email@gmail.com'
    recipients = ['shraddha@aviato.consulting', 'pooja@aviato.consulting']
    msg['To'] = ", ".join(recipients)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('sender_email@gmail.com', 'abcd wxyz efgh mnop')
            server.sendmail('sender_email@gmail.com', recipients, msg.as_string())
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to send email")

    return {"detail": "Invitation sent"}