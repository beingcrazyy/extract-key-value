from app.agent.agent import create_agent
from app.agent.prompt import PROMPT_TEMPLATE, NORMALIZE_PROMPT_TEMPLATE
from app.pipeline.run import run_pipeline

extract_agent = create_agent(PROMPT_TEMPLATE)
normalize_agent = create_agent(NORMALIZE_PROMPT_TEMPLATE)

result = extract_agent.invoke("Selling a baby feeding set which includes two bottles, one of 250 ml and one of 300 ml. Both are plastic, transparent, used for around 4 months. Sterilized regularly. Condition is good. No leaks.")
final_result = normalize_agent.invoke(result)

print(result.model_dump())
print(final_result.model_dump())


run_pipeline("Selling a baby feeding set which includes two bottles, one of 250 ml and one of 300 ml. Both are plastic, transparent, used for around 4 months. Sterilized regularly. Condition is good. No leaks.")