from pydantic import BaseModel, EmailStr, Field


# Properties required during user creation
class UserCreate(BaseModel):
    email : EmailStr
    password : str = Field(..., min_length=4)
    
    
    
class ShowUser(BaseModel):
    id: int
    email: EmailStr
    is_active : bool
    
    class ConfigDict():
        from_attributes = True