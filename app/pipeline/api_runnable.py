from langchain_core.runnables import RunnableLambda
from app.agent.agent import create_agent
from app.pipeline.retry_controller import run_with_retry

def run_api(extract_agent, normalize_agent, self_correction_agent):
    def pipeline(input:dict):
        text = input["input"]

        extracted = run_with_retry(
            extract_agent,
            self_correction_agent,
            text
        )

        print("Got extracted pairs :", extracted.model_dump())

        if extracted.attributes:
            normalized = normalize_agent.invoke(extracted.attributes)
            print("Got Normalize pairs :", normalized.model_dump())
            extracted.attributes = normalized.attributes

        return extracted
    return RunnableLambda(pipeline)
