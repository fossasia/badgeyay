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


def update_firebase_password(uid, pwd):
    try:
        auth.update_user(
            uid=uid,
            password=pwd
        )
        return True
    except Exception as e:
        print(e)
        return False


def update_firebase_username(uid, username):
    try:
        auth.update_user(
            uid=uid,
            username=username
        )
        return True
    except Exception as e:
        print(e)
        return False
