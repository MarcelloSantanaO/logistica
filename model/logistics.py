from sqlalchemy import Column,String
from model.base_model import BaseModel
from sqlalchemy.orm import validates


class Logistic(BaseModel):
    __tablename__='logistic'
    name = Column(String(length=150), nullable=False)
    description = Column(String(length=300), nullable=True)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError('Name must be string.')
        elif not name.strip():
            raise ValueError("Name can't be empty")
        elif len(name) > 150:
            raise ValueError('Name has exceeded the 150 characters.')
        return name

    @validates('description')
    def validate_description(self, key, description):
        if description is None:
            return description
        elif len(description) > 300:        
            raise ValueError('Description has exceeded the 300 characters.')
        return description    
        
