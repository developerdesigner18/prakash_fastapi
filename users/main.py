from fastapi import APIRouter, status, Depends, HTTPException   
from .schemas import userCreate
from .crud import create_user, dbOTP
from sqlalchemy.orm import Session
from dependencies import get_db
from .models import User, user_auth_otp
from fastapi.responses import JSONResponse
from helpers import IsValidEmail, IsValidNumber, ComplexPasswordValidatorFunc, IsDateValid, generateOTP
from send_mails import send_mail

router = APIRouter(

    prefix="/user"

)

@router.get("/check")
def checking_func():
    return {"hello":"world"}

@router.post("/signup")
async def user_signup(user_data:userCreate, db: Session = Depends(get_db)):

    if not IsValidEmail(user_data.email):
        raise HTTPException(status_code=406, detail="Please Provide Valid Email")
    
    if IsDateValid(user_data.date_of_birth):
        raise HTTPException(status_code=406, detail="Incorrect data format, should be YYYY-MM-DD")
    
    if not IsValidNumber(user_data.phone_no):
        raise HTTPException(status_code=406, detail="Please Provide Valid Phone no")
    
    if not ComplexPasswordValidatorFunc(user_data.password):
        raise HTTPException(status_code=406, detail="Password Should Contain 8 Chaacters of length, One Upper Case, One Lower Case, One Number and One Special Characters.")

    user_e = db.query(User).filter(User.email == user_data.email).first()
    user_p = db.query(User).filter(User.phone_no == user_data.phone_no).first()

    if user_e:
        raise HTTPException(status_code=409, detail="Email Already Exixts")
    elif user_p:
        raise HTTPException(status_code=409, detail="Phone No Already Exixts")
    else:
        user = create_user(db, user_data)
        return JSONResponse(status_code=201, content="User Created Successfully")
    
@router.post("/emailVerify")
async def email_verify(email: str , db: Session = Depends(get_db)):

    if not IsValidEmail(email):
        raise HTTPException(status_code=406, detail="Please Provide Valid Email")

    user_e = db.query(User).filter(User.email == email).first()

    if user_e:
        subject = "Email Verification OTP"
        email_recipients_list = [email]
        otp = generateOTP()
        templatevars = {    
            "otp":otp
        }
        template_name = "email_otp.html"

        storeDbOtp = dbOTP(db, email=email, otp=otp)

        await send_mail(subject=subject, email_to=email_recipients_list, templatevars=templatevars, template_name=template_name)

    else:
        return HTTPException(status_code=404, detail="Email Not Exists")