import requests

WEBHOOK_URL = "https://chat.googleapis.com/v1/spaces/AAQAeXJDSGQ/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=zPccHDqiznXhONGfK8x5bQBawydY9mOf3OqPcMigo9Q"

payload = {
    "text": "This is a test message."
}

response = requests.post(WEBHOOK_URL, json=payload)

print(response.status_code)
print(response.text)
