from app.agent.agent import create_agent
from app.agent.prompt import PROMPT_TEMPLATE, NORMALIZE_PROMPT_TEMPLATE

def run_pipeline(input):
    extracted = create_agent(PROMPT_TEMPLATE).invoke(input)
    print("Got extracted pairs :", extracted.model_dump())
    if not extracted.attributes:
        return extracted
    normalized = create_agent(NORMALIZE_PROMPT_TEMPLATE).invoke(extracted.attributes)
    print("Got Normalize pairs :", normalized.model_dump())
    extracted.attributes = normalized.attributes
    return extracted

