from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

messages = [
    SystemMessage(content="you are a helpful assistant"),
    HumanMessage(content="tell me about langchain")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)

