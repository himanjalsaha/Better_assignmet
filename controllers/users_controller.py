from services.user import user_services  
from flask import request, jsonify
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()

class user_controller:
    @staticmethod
    
    def create_table():
        """Create the user table."""
        user_services.create_user_table()

    @staticmethod
    def get_users():
        """Retrieve all users."""
        users = user_services.get_users()
        return jsonify([ {key: value for key, value in user.to_dict().items() if key != "password"} 
        for user in users]), 200

    @staticmethod
    def add_user():
        """Add a new user."""
        data = request.json
        username = data.get("username", "").strip()
        email = data.get("email", "").strip()
        password = data.get("password", "").strip()

        if not email or not password or not username:
            return jsonify({"error": "Username, email, and password are required"}), 400

        try:
            # Hash the password using bcrypt
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            user_services.add_user(username, email, hashed_password)
            return jsonify({"message": "User added successfully"}), 201
        except Exception as e:
            return jsonify({"error": f"Failed to add user: {str(e)}"}), 500

    @staticmethod
    def login():
        """Log in a user."""
        data = request.json
        email = data.get("email", "").strip()
        password = data.get("password", "").strip()

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        try:
            # Fetch user by email
            user = user_services.get_user_by_email(email)
            if not user:
                return jsonify({"error": "Invalid email or password"}), 401

            stored_password = user["password"]

     
            if not bcrypt.check_password_hash(stored_password, password):
                return jsonify({"error": "Invalid email or password"}), 401
            print(user["id"],email)
            token= user_services.generate_token(user["id"],email)
            
            return jsonify({"message": "Login successful", "token": token}), 200
        except Exception as e:
            return jsonify({"error": f"Failed to log in: {str(e)}"}), 500
