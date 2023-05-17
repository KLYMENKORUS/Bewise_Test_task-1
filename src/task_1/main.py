from fastapi import FastAPI, APIRouter
from api.handlers import router


app = FastAPI()

# create the instance for the routes
main_api_router = APIRouter()

# set routes to the app instance
main_api_router.include_router(
    router, prefix='/questions', tags=['questions']
)
app.include_router(main_api_router)