from pydantic import BaseModel
from typing import List,Dict
class Test(BaseModel):
    author: str
    book: str
    allBooks: Dict[str,str]


class Test1(BaseModel):
    userText: str
    allBooks: Dict[str,str]
