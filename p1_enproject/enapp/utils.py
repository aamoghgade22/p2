from datetime import datetime, timedelta

def custom_jwt_payload_handler(user):
    payload = {
        'user_id': user.id,
        'username': user.username,
        'email': user.email,
        'exp': datetime.utcnow() + timedelta(hours=24),  # custom expiration time
        'is_admin': user.is_staff,  # custom claim
    }
    return payload
