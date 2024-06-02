from pydantic import BaseModel, EmailStr, Field


# Properties required during user creation
class UserCreate(BaseModel):
    email : EmailStr
    password : str = Field(..., min_length=4)
    
    
    