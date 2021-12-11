def validate_name_len(name):
    if len(name) <= 1:
        return True
    return False

def validate_email(email):
    if '@' not in email or '.com' not in email:
        return True
    return False

def validate_password(password):
    if len(password) < 8:
        return True
    return False
