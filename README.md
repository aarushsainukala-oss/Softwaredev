# 📱 WhatsApp GPT Chatbot

This is a simple AI-powered WhatsApp chatbot built with Flask, Twilio, and OpenAI GPT.

---

## 🚀 Features
- Replies to WhatsApp messages with GPT-3.5-turbo.
- Remembers the last few messages (conversation memory).
- Runs locally with ngrok + Twilio sandbox.

---

## 🛠️ Installation & Setup

### 1. Clone this repo
```bash
git clone <your-repo-url>
cd whatsapp-gpt-bot
2. Install dependencies
pip install -r requirements.txt
3. Configure your API key

Copy .env.example → .env

Add your OpenAI key:
OPENAI_API_KEY=sk-your-api-key-here
4. Run flask
python app.py
You should see:
 * Running on http://127.0.0.1:5000
5. Start ngrok
ngrok http 5000
6. Configure Twilio
Go to Twilio WhatsApp Sandbox

In “When a message comes in”, paste:
https://xxxx.ngrok.io/whatsapp
7. Test it 🎉

Send "Hi" to your Twilio sandbox WhatsApp number.

GPT will reply.
Example Conversation

You: Hi
Bot: Hello! How can I help you today?

You: My name is Aarush
Bot: Nice to meet you, Aarush!
Notes:
ngrok gives a new URL each time you restart — update Twilio’s webhook if it changes.
Do not share your .env file or real API key publicly.

video:https://drive.google.com/drive/folders/1dvO-H6bH3M9tZyE4X0mG3UhaDvOvHR35?usp=sharing