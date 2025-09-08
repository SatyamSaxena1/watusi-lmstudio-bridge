WhatsApp Auto-Reply with LM Studio (Local LLM)

Overview
- Flask webhook that accepts Watusi Auto-Reply POSTs and generates replies via LM Studio's OpenAI-compatible API. Incoming text is sent verbatim to the model; the model's reply is returned verbatim as JSON.

Prereqs
- LM Studio running on your machine with a single model loaded
  - Server reachable at e.g. http://192.168.80.1:1234
- Python 3.10+

Install
1) Create / activate a venv (recommended)
2) Install deps

Run
1) Set env vars if your LM Studio host/port/model differ
	- LM_STUDIO_HOST, LM_STUDIO_PORT, LM_STUDIO_MODEL, LM_TEMPERATURE, LM_MAX_TOKENS, LM_REQUEST_TIMEOUT
	- Optionally restrict to specific chat(s) by setting ALLOWED_JIDS to a comma-separated list of JIDs (e.g. "12225557777@s.whatsapp.net").
2) Start the server
	- python app.py
3) Test locally
	- python test_client.py  # posts to http://localhost:8000/auto-reply

Configure Watusi
- Message Source: Web
- URL: http://<your_pc_ip>:8000/auto-reply
- Response format: JSON { "message": "..." }

Notes
- In-memory conversation memory (last ~8 messages per JID). Restart clears history.
- Replies are generated entirely by the model; there is no injected system prompt.
- Ensure your phone can reach your PC's IP and that Windows Firewall allows inbound on the chosen port (default 8000) for Private network.
- LM_REQUEST_TIMEOUT controls how long we wait for LM Studio to answer per request.
