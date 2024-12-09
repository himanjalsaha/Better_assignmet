from flask import request, jsonify
import jwt
from dotenv import load_dotenv
import os
from services.user import user_services

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")


def token_required(f):
    """Decorator to verify the JWT token."""
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Token is missing or invalid"}), 401
        
        token = auth_header.split(" ")[1]
        try:
            # Decode the JWT token
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            user_id = payload.get("user_id")

            # Optionally, you can fetch user details from the database if needed
            user = user_services.get_user_by_id(user_id)
            if not user:
                return jsonify({"error": "User not found"}), 401
            
            # Attach user info to the request for use in the endpoint
            request.user = user
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

        return f(*args, **kwargs)
    return wrapper
