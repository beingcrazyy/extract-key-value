from langchain_core.exceptions import OutputParserException

MAX_RETRIES = 3

def run_with_retry(agent, self_correction_agent, input_text):
    last_error = None
    last_output = None

    for attempt in range(MAX_RETRIES):
        try:
            result = agent.invoke(input_text)
            return result
        except OutputParserException as e:
            last_error = str(e)
            last_output = getattr(e, "llm_output", None)

            if attempt == MAX_RETRIES - 1:
                raise e
            
            correction_payload = {
                "input" : input_text,
                "error" : last_error,
                "output" : last_output
            }

            agent = self_correction_agent.bind(**correction_payload)
    
    raise RuntimeError("Retry Machanism failed unexpectedly")


