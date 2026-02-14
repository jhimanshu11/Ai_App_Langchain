from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation" 
)
model = ChatHuggingFace(llm=llm)

chat_template = ChatPromptTemplate.from_messages(
    [
        ('system', "You are helpful {domain} expert"),
        ('human', "Explain about {topic} games"),
    ]
)

prompt = chat_template.invoke({'domain': 'Games Expert', 'topic': 'Cricket'})
print(prompt)