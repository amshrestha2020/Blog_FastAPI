from typing import Optional
from pydantic import BaseModel, field_validator
from datetime import date



class CreateBlog(BaseModel):
    title: str 
    slug: Optional[str] 
    content: Optional[str] = None 
    
    @field_validator('slug')
    def generate_slug(cls, values):
        if 'title' in values and 'slug' not in values:
            values['slug'] = values.get("title").replace(" ","-").lower()
        return values
        
#new addition
class UpdateBlog(CreateBlog):    
    pass

        
class ShowBlog(BaseModel):
    title:str 
    content: Optional[str]
    created_at: date

    class ConfigDict():
        from_attributes = True