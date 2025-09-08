import json
import requests

payload = {
    "date": "2025-09-08 10:00:00",
    "jid": "12345@s.whatsapp.net",
    "name": "Alice",
    "text": "Hey! Are you free for lunch today?"
}

resp = requests.post("http://127.0.0.1:8000/auto-reply", json=payload, timeout=10)
print(resp.status_code)
print(resp.headers.get('content-type'))
print(json.dumps(resp.json(), indent=2))
