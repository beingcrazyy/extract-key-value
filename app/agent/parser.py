from langchain_core.output_parsers import PydanticOutputParser
from app.agent.schema import ExtractedData

def get_output_parser() -> PydanticOutputParser:
    
    """
    Return the PydanticOutputParser with the required Schema
    """
    return PydanticOutputParser(pydantic_object=ExtractedData)