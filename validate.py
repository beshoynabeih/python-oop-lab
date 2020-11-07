import re
import json
from user import User

#load all user to check email and mobile number duplicated values

def validate_f_name(f_name):
    if not f_name or not re.match("^[a-z]+$", f_name):
        return "invalid first name"
    return True

def validate_l_name(l_name):
    if not l_name or not re.match("^[a-z]+$", l_name):
        return "Invalid last name"
    return True

def unique_field(field, value):
    users = User.get_users()
    for user in users:
        if user[field] == value.strip():
            return False
    return True
    
def validate_email(email):
    if not email or not re.match("^[a-zA-Z]+[a-z-A-Z0-9-_\.]*@[a-zA-z]{2,6}\.[a-zA-z]{2,3}$", email) or not unique_field("email", email):
        return False
    return True

def validate_password(password):    
    if not password or len(password) < 6 or password.isdigit() or password.isalpha():
        return "Invalid Password"
    return True

def validate_conf_pass(conf_pass, password):
    if not conf_pass or password != conf_pass:
        return "Password does not match"
    return True
    
def validate_mobile(mobile):
    if not mobile or not re.match("^(010|011|012|015)[0-9]{8}$", mobile) or not unique_field("mobile", mobile):
        return "Invalid Mobile Number"
    return True

def validate_string(str_var):
    if not str_var or not re.match("^[a-zA-Z\s]+$", str_var):
        return False
    return True

def validate_date(date):
    return re.match("^[0-3]?[0-9]{1}-[0|1]?[0-9]{1}-[0-9]{4}$", date)
        

#check for unique and phone values