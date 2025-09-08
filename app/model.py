from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Post(BaseModel):
    id : Optional[str] = Field(None, alias="_id")
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    slug: str 
    title: str
    desc: str
    content: str
    img: Optional[str]=None

    class Config:
        populate_by_name: True
        json_schema = {
            "ex" : {
                "slug" : "ex post",
                "title" : "rise of the r",
                "desc" : "the un des pu ",
                "img" : "https://gugu.com/nunu.png",
                "content" : "exo exo ;3"
            }
        }

class PostUpdate(BaseModel):
    id : Optional[str] = Field(None, alias="_id")
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    slug: str 
    title: str
    desc: str
    content: str
    img: Optional[str]=None