from pydantic import BaseModel, EmailStr
from typing import Annotated
from annotated_types import MaxLen, MinLen

class CreateUser(BaseModel):
    name: Annotated[str, MaxLen(50), MinLen(1)]
    email: EmailStr