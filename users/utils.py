import requests
from django.utils import timezone
from django.conf import settings


def send_verification_code(phone, code):
    message_id = str(timezone.now()) # noqa
    requests.post(
        settings.SMS_URL,
        auth=(settings.SMS_LOGIN, settings.SMS_PASSWORD),
        json={
            "messages": [
                {
                    "recipient": str(phone),
                    "message-id": message_id,
                    "sms": {
                        "originator": "3700",
                        "content": {
                            "text": f"SoffStudy.uz <#> Your verification code is {code}"
                        },
                    },
                }
            ]
        },
    )


