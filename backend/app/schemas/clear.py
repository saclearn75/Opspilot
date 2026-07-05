from pydantic import BaseModel

class ClearResponse(BaseModel):
    message: str