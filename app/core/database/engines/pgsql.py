from sqlalchemy import create_engine
from dotenv import load_dotenv

from ..dburl import url

engine = create_engine(
    url=url,
    pool_size=5,
    pool_pre_ping=True,  # Проверять соединение перед использованием
)
