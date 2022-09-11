from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    titles: str
    image: str
    description: str
    tags: List[str]
    location:str
    
    class Config:
        schema_extra = {
            "example":{
                "title": "FastApi Book Launch",
                "image":"hhtps://linkstomyimage.com/image.png",
                "description": "We will be discussing the contents of the FASTAPI book in this event ",
                "tags": ["python","fastapi","book","launch"],
                "location":"Google Meet"
            }
        }
