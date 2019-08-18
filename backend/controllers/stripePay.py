import stripe
from flask import Blueprint, jsonify, request
from api.models.user import User
from api.schemas.operation import StripePaymentSchema
from api.utils.errors import ErrorResponse
from api.schemas.errors import (
    PayloadNotFound,
    OperationNotFound
)


router = Blueprint('stripPay', __name__)


@router.route('/payment', methods=['POST'])
def stripe_payment():
    try:
        data = request.get_json()
    except Exception:
        return ErrorResponse(PayloadNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    try:
        token = data['stripe_refresh_token']
    except Exception:
        return ErrorResponse(PayloadNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    try:
        charge = stripe.Charge.create(
            amount=data['amount'],
            currency=data['currency'],
            customer=data['stripe_user_id'],
            source=token
        )
        user = User.getUser(user_id=data['uid'])
        resp = {
            'id': user.id,
            'charge': charge
        }
        resp['status'] = 'Charge Created'
    except Exception:
        return ErrorResponse(OperationNotFound().message, 422, {'Content-Type': 'application/json'}).respond()

    return jsonify(StripePaymentSchema().dump(resp).data)
