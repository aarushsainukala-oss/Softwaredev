from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from langchain_openai import ChatOpenAI

app = Flask(__name__)

# 🔴 TEMPORARY: Hardcode API key for testing
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    openai_api_key="Your_API_key"
)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "")
    print("Incoming:", incoming_msg)  # debug log

    try:
        ai_reply = llm.predict(incoming_msg)
    except Exception as e:
        ai_reply = f"Error while calling GPT: {e}"

    resp = MessagingResponse()
    resp.message(ai_reply)
    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)





