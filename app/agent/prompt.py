from langchain_core.prompts import PromptTemplate

PROMPT_TEMPLATE = """
    You are an information extraction agent.

    Your task is to extract key–value pairs ONLY from the user's input.

    Rules:
    
    - Do NOT infer or assume missing information.
    - Do NOT add attributes that are not explicitly mentioned.
    - If something is not mentioned, do not include it.
    - Return JSON only.
    - Follow the output format strictly.

    User input:
    {input}

    {format_instructions}
"""



NORMALIZE_PROMPT_TEMPLATE = """
    You are a normalization agent.

    Your task is to map extracted attribute keys to the closest semantically correct canonical keys.

    Canonical keys you are allowed to use:
    - product_type
    - brand
    - model
    - size
    - dimensions
    - weight
    - capacity
    - material
    - color
    - pattern
    - condition
    - used_duration
    - usage_frequency
    - age_range
    - quantity
    - set_includes
    - count
    - compatible_with
    - recommended_for
    - safety_certification
    - age_restriction
    - features
    - defects
    - maintenance_history

    Rules:
    1. You may ONLY rename keys or normalize values.
    2. Do NOT invent new attributes.
    3. Do NOT infer missing information.
    4. If an attribute does not clearly map to a canonical key, keep it unchanged.
    5. Do NOT drop attributes unless they are duplicates after normalization.
    6. Return JSON only.
    7. Follow the output format strictly.

    Example:
    Input:
    "size": "S",
    "worn": "twice"
    

    Output:
    "size": "S",
    "condition": "Lightly Used"

    User input:
    {input}

    {format_instructions}
"""
