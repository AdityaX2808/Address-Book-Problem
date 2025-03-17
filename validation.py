import re

def input_wrapper(validation_func):
    def wrapper(prompt):
        while True:
            user_input = input(prompt).strip()
            if validation_func(user_input):
                return user_input
            print(f"Invalid input! Please try again.")
    return wrapper

@input_wrapper
def validate_first_name(name):
    return bool(re.match(r"^[A-Za-z\s]+$", name))

@input_wrapper
def validate_last_name(name):
    return bool(re.match(r"^[A-Za-z]+$", name))

@input_wrapper
def validate_address(address):
    return bool(re.match(r"^[A-Za-z0-9/,\-\s]+$", address))

@input_wrapper
def validate_city(city):
    return bool(re.match(r"^[A-Za-z]+$", city))

@input_wrapper
def validate_state(state):
    return bool(re.match(r"^[A-Za-z\s]+$", state))

@input_wrapper
def validate_zip_code(zip_code):
    return bool(re.match(r"^\d{5,6}$", zip_code))

@input_wrapper
def validate_phone_number(phone_number):
    return bool(re.match(r"^[6-9]\d{9}$", phone_number))

@input_wrapper
def validate_email(email):
    return bool(re.match(r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email))