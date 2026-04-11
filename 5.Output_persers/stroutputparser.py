from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# 1st prompt - detailed report
template1 = PromptTemplate(
    template = "write a detailed report on {topic}",
    input_variables=["topic"]
)

# 2nd prompt - summary
template2 = PromptTemplate(
    template = "write a 5 line summary on the following text." \
    "{text}",
    input_variables=["text"]
)


prompt1 = template1.invoke(
    {
        "topic": "blackhole"
    }
)

result = model.invoke(prompt1)

print(result)

prompt2 = template2.invoke(
    {
        "text": result.content
    }
)

final_result = model.invoke(prompt2)

print(final_result.content)


