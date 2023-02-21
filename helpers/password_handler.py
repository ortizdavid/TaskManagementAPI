from werkzeug.security import generate_password_hash, check_password_hash

class PasswordHandler:

    def generate(password):
        return generate_password_hash(password)

    def check(encrypted_password, pure_password):
        if check_password_hash(encrypted_password, pure_password):
            return True
        else:
            return False