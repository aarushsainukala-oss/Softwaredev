from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    openai_api_key="Your_API_Key"
)

print(llm.predict("Say hello in a fun way"))

