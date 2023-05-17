import typing
from datetime import datetime
from logging import getLogger
import requests
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_503_SERVICE_UNAVAILABLE
from api.schemas import ShowQuestion
from db.session import get_db
from api.optional import QuestionAction

logger = getLogger(__name__)

router = APIRouter()


def format_question(question: dict) -> ShowQuestion:
    """
    Форматируем вопрос для записи в бд
    :param question: Question
    :return: ShowQuestion
    """
    return ShowQuestion(
        question_id=question['id'],
        category_id=question['category_id'],
        question_text=question['question'],
        answer_text=question['answer'],
        created_at=datetime.strptime(
            question['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ'
        ).date()

    )


@router.post('/', description='creating a new question in the database')
async def create_question(
        questions_num: int = 1,
        session: AsyncSession = Depends(get_db)
) -> ShowQuestion | typing.Dict:
    """
    Хендлер создания нового вопроса в бд
    :param questions_num: количество вопросов
    :param session: текущая сессия
    :return: Созданные вопросы
    """
    try:

        response_q = {
            'status': 200,
            'last_question': None
        }

        # получаем последний сохраненный вопрос если он сущесвует
        last_question = await QuestionAction.last_question(session)
        last_question = response_q if last_question is None else last_question

        logger.info(f'last_question {last_question}')

        response = requests.get(
            url=f'https://jservice.io/api/random?count={questions_num}'
        )

        for question in response.json():
            # делаем запрос к бд для проверки на уникальность
            get_question = await QuestionAction.get_question_by_id(
                question['id'], session
            )
            # если в бд существует данный вопрос просто ищем другой
            while get_question:
                question = requests.get(
                    url='https://jservice.io/api/random?count=1'
                ).json()[0]
            await QuestionAction.create_question(format_question(question), session)

            logger.info(f'Question is id {question["id"]} successfully added to database')

        return last_question

    except IntegrityError as err:
        raise HTTPException(
            status_code=HTTP_503_SERVICE_UNAVAILABLE,
            detail=f'Database error {err}'
        )
