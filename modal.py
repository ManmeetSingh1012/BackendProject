from pydantic import BaseModel

class Todo(BaseModel):
    name:str
    designation:str