from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):

    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    email = Column(String, unique=True, index=True)
    phone_no = Column(String, unique=True,)
    is_email_verified = Column(Boolean, default=False)
    user_role = Column(String, default='user')
    password = Column(String)
    date_of_joining = Column(DateTime, default= datetime.now() )
    last_login = Column(DateTime, nullable=True)

class user_auth_otp(Base):

    __tablename__ = "UserauthOTP"

    id = Column(Integer, primary_key=True, index=True)
    OTP = Column(String)
    user = relationship("User", back_populates="email")


