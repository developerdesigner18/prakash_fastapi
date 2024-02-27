from fastapi import Depends, FastAPI, HTTPException, APIRouter

from database import engine

from users import models as userModels
from users import main as userRouter

userModels.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(userRouter.router)