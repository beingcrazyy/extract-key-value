from langchain_core.runnables import RunnableLambda
from app.agent.agent import create_agent
from app.agent.prompt import PROMPT_TEMPLATE, NORMALIZE_PROMPT_TEMPLATE

def run_api(extract_agent, normalize_agent):
    def pipeline(input:str):
        extracted = extract_agent.invoke(input)
        print("Got extracted pairs :", extracted.model_dump())

        if extracted.attributes:
            normalized = normalize_agent.invoke(extracted.attributes)
            print("Got Normalize pairs :", normalized.model_dump())
            extracted.attributes = normalized.attributes

        return extracted
    return RunnableLambda(pipeline)
