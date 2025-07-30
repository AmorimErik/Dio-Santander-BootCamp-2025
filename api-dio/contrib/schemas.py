from datetime import datetime
from pydantic import UUID4, BaseModel, Field
from typing import Annotated

class BaseSchema(BaseModel):
    class Config:
        extra = 'forbird'
        from_attributes = True

class OutMixin(BaseSchema):
    id: Annotated[UUID4, Field(description='Identificador')]
    created_at: Annotated[datetime, Field(description='Data de criação')]