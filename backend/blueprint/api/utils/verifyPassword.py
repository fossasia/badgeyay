from werkzeug.security import check_password_hash


def verifyPassword(user, password):
    return check_password_hash(
        user.password,
        password)
