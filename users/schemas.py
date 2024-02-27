from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional
import re

class userBase(BaseModel):
    email: str
    phone_no: str

class userCreate(userBase):
    first_name: str
    last_name: str
    date_of_birth: date
    password: str