import uuid
from sqlalchemy import Column, Text, Integer, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class Question(Base):
    __tablename__ = 'questions'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_id = Column(Integer, nullable=False, unique=True)
    category_id = Column(Integer, nullable=False)
    question_text = Column(Text)
    answer_text = Column(Text)
    created_at = Column(Date, default=None)