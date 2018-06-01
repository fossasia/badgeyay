from flask import Blueprint, jsonify, request
from api.utils.response import Response
from firebase_admin import auth


router = Blueprint('users', __name__)


@router.route('/createuser', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify(Response(500).generateMessage(str(e)))

    try:
        user = auth.create_user(
            display_name=data['name'],
            email=data['email'],
            email_verified=data['email_verified'],
            photo_url=data['photo_url'],
            password=data['password'],
            disabled=data['disabled']
        )
        return jsonify(Response(200).generateMessage('Sucessfully created new user named {0} with user-id: {1}'.format(user.display_name, user.uid)))
    except Exception as e:
        return jsonify(Response(400).generateMessage(str(e)))


@router.route('/updateuser', methods=['POST'])
def update_user():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify(Response(500).generateMessage(str(e)))

    try:
        user = auth.update_user(
            data['uid'],
            display_name=data['name'],
            email=data['email'],
            email_verified=data['email_verified'],
            photo_url=data['photo_url'],
            password=data['password'],
            disabled=data['disabled']
        )
        return jsonify(Response(200).generateMessage('Sucessfully updated user: {0}'.format(user.uid)))
    except Exception as e:
        return jsonify(Response(400).generateMessage(str(e)))


@router.route('/deleteuser', methods=['POST'])
def delete_user():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify(Response(500).generateMessage(str(e)))

    try:
        auth.delete_user(
            data['uid']
        )
        return jsonify(Response(200).generateMessage('Successfully deleted user'))
    except Exception as e:
        return jsonify(Response(400).generateMessage(str(e)))


@router.route('/user/<uid>/userdetails', methods=['GET'])
def get_user_details(uid):
    try:
        user_details = auth.get_user(uid)
        name = user_details.display_name
        email = [{'address': user_details.email, 'verified': user_details.email_verified}]
        photo_url = user_details.photo_url
        provider_id = user_details.provider_id
        disabled = user_details.disabled
        custom_claims = user_details.custom_claims

        return jsonify({
            'name': name,
            'email': email,
            'photo_url': photo_url,
            'provider_id': provider_id,
            'disabled': disabled,
            'custom_claims': custom_claims
        })
    except Exception as e:
        return jsonify(Response(400).generateMessage(str(e)))


@router.route('/listusers', methods=['GET'])
def list_users():
    try:
        page = auth.list_users()
        users_list = []
        while page:
            for user in page.users:
                users_list.append(user.uid)
            page = page.get_next_page()
        return jsonify({
            'total_users': len(users_list),
            'users': users_list
        })
    except Exception as e:
        return jsonify(Response(400).generateMessage(str(e)))


@router.route('/user/<uid>/displayname', methods=['GET'])
@router.route('/user/<uid>/email', methods=['GET'])
@router.route('/user/<uid>/usermetadata', methods=['GET'])
def get_details(uid):
    try:
        user_details = auth.get_user(uid)
        if 'displayname' in request.path:
            return jsonify({
                'name': user_details.display_name,
            })
        elif 'email' in request.path:
            return jsonify({
                'email': [{'address': user_details.email, 'verified': user_details.email_verified}],
            })
        elif 'usermetadata' in request.path:
            return jsonify({
                'creation timestamp': user_details.user_metadata.creation_timestamp,
                'last signin timestamp': user_details.user_metadata.last_sign_in_timestamp
            })

    except Exception as e:
        return jsonify(Response(400).generateMessage(str(e)))


@router.route('/user/<email>/userdetails', methods=['GET'])
def get_user_details_by_email(email):
    try:
        user_details = auth.get_user_by_email(email)
        name = user_details.display_name
        email = [{'address': user_details.email, 'verified': user_details.email_verified}]
        photo_url = user_details.photo_url
        provider_id = user_details.provider_id
        disabled = user_details.disabled
        custom_claims = user_details.custom_claims

        return jsonify({
            'name': name,
            'email': email,
            'photo_url': photo_url,
            'provider_id': provider_id,
            'disabled': disabled,
            'custom_claims': custom_claims
        })
    except Exception as e:
        return jsonify(Response(400).generateMessage(str(e)))


@router.route('/user/<email>/displayname', methods=['GET'])
@router.route('/user/<email>/email', methods=['GET'])
@router.route('/user/<email>/usermetadata', methods=['GET'])
def get_details_by_email(email):
    try:
        user_details = auth.get_user_by_email(email)
        if 'displayname' in request.path:
            return jsonify({
                'name': user_details.display_name,
            })
        elif 'email' in request.path:
            return jsonify({
                'email': [{'address': user_details.email, 'verified': user_details.email_verified}],
            })
        elif 'usermetadata' in request.path:
            return jsonify({
                'creation timestamp': user_details.user_metadata.creation_timestamp,
                'last signin timestamp': user_details.user_metadata.last_sign_in_timestamp
            })

    except Exception as e:
        return jsonify(Response(400).generateMessage(str(e)))


@router.route('/update/user/name', methods=['POST'])
@router.route('/update/user/email', methods=['POST'])
@router.route('/update/user/password', methods=['POST'])
@router.route('/update/user/disable', methods=['POST'])
def update_user_detail():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify(Response(500).generateMessage(str(e)))

    try:
        if 'name' in request.path:
            user = auth.update_user(
                data['uid'],
                display_name=data['name']
            )
        elif 'email' in request.path:
            user = auth.update_user(
                data['uid'],
                email=data['email'],
                email_verified=data['email_verified']
            )
        elif 'password' in request.path:
            user = auth.update_user(
                data['uid'],
                password=data['password']
            )
        elif 'disable' in request.path:
            user = auth.update_user(
                data['uid'],
                disabled=data['disabled']
            )
        return jsonify(Response(200).generateMessage('Sucessfully updated user: {0}'.format(user.uid)))
    except Exception as e:
        return jsonify(Response(400).generateMessage(str(e)))
