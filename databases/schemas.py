from pydantic import BaseModel

class UserForm(BaseModel):
    email: str
    password: str


class UserResp(BaseModel):
    email: str
    name: str
    class Config:
        orm_mode = True