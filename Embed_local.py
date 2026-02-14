from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents=[
    "Delhi is capital of india",
    "Delhi is city",
    "Boom Boom delhi"
]


vector =embedding.embed_query(documents)
print(str(vector))
