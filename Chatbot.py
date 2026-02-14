from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation" 
)
model = ChatHuggingFace(llm=llm)

chat_history = [
    SystemMessage(content="I am smart AI agent")
]
while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    
    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:", result.content)
print(chat_history)