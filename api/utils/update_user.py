from firebase_admin import auth


def update_firebase_photoURL(uid, photoURL):
    try:
        auth.update_user(
            uid=uid,
            photoURL=photoURL
        )
        return True
    except Exception as e:
        print(e)
        return False


def update_firebase_emailVerified(uid):
    try:
        auth.update_user(
            uid=uid,
            email_verified=True
        )
        return True
    except Exception as e:
        print(e)
        return False


def update_firebase_password(uid, _pwd):
    try:
        auth.update_user(
            uid=uid,
            password=_pwd
        )
        return True
    except Exception as e:
        print(e)
        return False


def update_firebase_username(uid, username):
    try:
        auth.update_user(
            uid=uid,
            display_name=username
        )
        return True
    except Exception as e:
        print(e)
        return False


def update_firebase_email(uid, email):
    try:
        auth.update_user(
            uid=uid,
            email=email
        )
        return True
    except Exception as e:
        print(e)
        return False


def update_firebase_complete(uid, username, email, _pwd):
    try:
        if _pwd != '':
            ret = update_firebase_password(uid, _pwd)
        if email != '':
            ret = update_firebase_email(uid, email)
        if username != '':
            ret = update_firebase_username(uid, username)
        print(ret)
        return True
    except Exception as e:
        print(e)
        return False
