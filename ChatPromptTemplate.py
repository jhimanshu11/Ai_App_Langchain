from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation" 
)
model = ChatHuggingFace(llm=llm)

# Fixed syntax for ChatPromptTemplate
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {domain} expert"),
    ("human", "Kindly explain about {bimari} symptoms")
])

# Invoke the template to format messages
result = chat_template.invoke({'domain': 'medicine', 'bimari': 'malaria'})
print(result)

# To actually get AI response, you need to pass the formatted messages to the model
response = model.invoke(result)
print(response)