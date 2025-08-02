from configs.database import get_session
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

DatabaseDependency = Annotated[AsyncSession, Depends(get_session)]