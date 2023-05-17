from datetime import datetime
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Question


class QuestionDAL:
    """
    Уровень доступа над операциями 'Question'
    """

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_question(
            self, question_id: int, category_id: int, question_text: str,
            answer_text: str, created_at: datetime
    ) -> Question:
        """
        Создание нового вопроса в бд
        :param question_id: id вопроса
        :param category_id: id категории
        :param question_text: текст вопроса
        :param answer_text: текст ответа
        :param created_at: дата создания вопроса
        :return: Question
        """
        new_question = Question(
            question_id=question_id,
            category_id=category_id,
            question_text=question_text,
            answer_text=answer_text,
            created_at=created_at
        )
        self.db_session.add(new_question)
        await self.db_session.flush()

        return new_question

    async def get_question_by_id(self, question_id: int) -> Question | None:
        """
        Получение вопроса по id
        :param question_id: id вопроса
        :return: Question | None
        """
        query = select(Question).\
            where(and_(Question.question_id == question_id))

        result = await self.db_session.execute(query)
        get_question = result.fetchone()

        return None if get_question is None else get_question[0]

    async def last_question(self) -> Question | None:
        """
        Получение последнего сохраненного вопроса
        :return: Question | None
        """
        query = select(Question).order_by(Question.id.desc()).limit(1)

        result = await self.db_session.execute(query)
        question = result.fetchone()

        return None if question is None else question[0]
