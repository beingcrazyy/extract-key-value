from typing import Dict, Optional
from pydantic import BaseModel, Field

class ExtractedData(BaseModel):
    """
    Schema for key-value pair extracted
    """

    product_type : Optional[str] = Field(
        default= None,
        description="The type of item explicitly mentioned by the user (e.g. jeans, bag, stroller)"
    )

    attributes : dict[str,str] = Field(
        default=dict,
        description="A dictionary of attributes and their corresponding values mentioned by the user"
    )

class Config:
    extra = 'forbid'
