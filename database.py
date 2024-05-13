from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import settings

# Database URL, typically from environment or configuration file
DATABASE_URL = settings.database_url
# Create the Async Engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Session factory bound to the engine
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

# Base class for models using the declarative system
Base = declarative_base()

# Dependency to get DB session
async def get_db_session():
    async with AsyncSessionLocal() as session:
        yield session
