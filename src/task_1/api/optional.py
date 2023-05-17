from api.schemas import ShowQuestion
from db.dal import QuestionDAL
from sqlalchemy.ext.asyncio import AsyncSession


class QuestionAction:
    """
    Класс для управления над действиями Question в бд
    """

    @classmethod
    async def create_question(
            cls, body: ShowQuestion, db_session: AsyncSession
    ) -> ShowQuestion:
        """
        Создание вопроса в бд
        :param body: обьект вопроса
        :param db_session: объект сессии
        :return: объект вопроса созданного в бд
        """
        async with db_session as session:
            async with session.begin():
                question_dal = QuestionDAL(session)
                new_question = await question_dal.create_question(
                    question_id=body.question_id,
                    category_id=body.category_id,
                    question_text=body.question_text,
                    answer_text=body.answer_text,
                    created_at=body.created_at
                )
                return ShowQuestion(
                    question_id=new_question.question_id,
                    category_id=new_question.category_id,
                    question_text=new_question.question_text,
                    answer_text=new_question.answer_text,
                    created_at=new_question.created_at
                )

    @classmethod
    async def get_question_by_id(
            cls, question_id: int, db_session: AsyncSession
    ) -> ShowQuestion | None:
        """
        Получение вопроса по его id
        :param question_id: id вопроса
        :param db_session: объект сессии
        :return: объект вопроса или None
        """
        async with db_session as session:
            async with session.begin():
                question_dal = QuestionDAL(session)
                question = await question_dal.get_question_by_id(question_id)

                return None if question is None else ShowQuestion(
                    question_id=question.question_id,
                    category_id=question.category_id,
                    question_text=question.question_text,
                    answer_text=question.answer_text,
                    created_at=question.created_at
                )

    @classmethod
    async def last_question(cls, db_session: AsyncSession) -> ShowQuestion | None:
        """
        Получение последнего сохраненного вопроса
        :param db_session: объект сессии
        :return: ShowQuestion | None
        """
        async with db_session as session:
            async with session.begin():
                question_dal = QuestionDAL(session)
                last_question = await question_dal.last_question()

                return None if last_question is None else ShowQuestion(
                    question_id=last_question.question_id,
                    category_id=last_question.category_id,
                    question_text=last_question.question_text,
                    answer_text=last_question.answer_text,
                    created_at=last_question.created_at
                )