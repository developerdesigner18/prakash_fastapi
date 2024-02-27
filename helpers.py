import re
import random
import string
import datetime

def IsDateValid(date_text):

    output = True

    try:
        datetime.date.fromisoformat(date_text)
        output = True
    except:
        output = False

    return output

def IsValidEmail(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.match(pattern, email):
        return True
    else:
        return False
    
def IsValidNumber(phone_no):

    pattern = r'^[6-9]\d{9}$'
    
    if re.match(pattern, phone_no):
        return True
    else:
        return False

def ComplexPasswordValidatorFunc(password):

    if re.search('[A-Z]', password)==None or re.search('[0-9]', password)==None or re.search('[^A-Za-z0-9]', password)==None or len(password) < 8:
        return False
    else:
        return True
    
def get_random_strong_password():

    random_source = string.ascii_letters + string.digits + string.punctuation
    # select 1 lowercase
    password = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    password += random.choice(string.ascii_uppercase)
    # select 1 digit
    password += random.choice(string.digits)
    # select 1 special symbol
    password += random.choice(string.punctuation)

    # generate other characters
    for i in range(8):
        password += random.choice(random_source)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)

    return password

def generateOTP(length=6):

    character_otp = string.ascii_letters + string.digits
    otp = ''.join(random.choice(character_otp) for i in range(6))
    return otp

