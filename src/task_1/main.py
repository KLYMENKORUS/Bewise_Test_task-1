from fastapi import FastAPI, APIRouter
from api.handlers import router


app = FastAPI(title='Task #1',
              description='Test tasks for bewise.ai')

# create the instance for the routes
main_api_router = APIRouter()

# set routes to the app instance
main_api_router.include_router(
    router, prefix='/questions', tags=['questions']
)
app.include_router(main_api_router)