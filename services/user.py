from queries.user_queries import user_queries
from models.User import UserModel
from utils import execute_query
from flask_bcrypt import Bcrypt
import jwt
from datetime import datetime, timedelta
bcrypt = Bcrypt()

SECRET_KEY = "dkjcbskjcbskjas"  
class user_services:
    @staticmethod
    def create_user_table():
        query = user_queries.create_users
        execute_query(query)
        
    @staticmethod
    def add_user(username, email, password):
     
        query = user_queries.add_user
        execute_query(query, (username, email, password))

    @staticmethod
    def get_users():
        query = "select * from users"    
        rows = execute_query(query, fetch=True)
        return [UserModel(row["id"], row["username"], row["email"], row["password"]) for row in rows]
    
    @staticmethod
    def get_user_by_email(email):
        query = "SELECT * FROM users WHERE email = ?"
        rows = execute_query(query, (email,), fetch=True)
        return rows[0] if rows else None
    
    @staticmethod
    def get_user_by_id(id):
        query = "SELECT * FROM users WHERE id = ?"
        rows = execute_query(query, (id,), fetch=True)
        return rows[0] if rows else None
        
    
   
     
    @staticmethod
    def generate_token(id,username):
      
        payload = {
            "user_id": id,
            "username": username,
            "exp": datetime.utcnow() + timedelta(hours=1)  # Token expires in 1 hour
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    
    @staticmethod
    def get_user_by_token(token, secret_key):
        try:
            decoded_token = jwt.decode(token,  secret_key, algorithms=["HS256"])
            return decoded_token  # Or you can return a user object, depending on your use case
        except jwt.ExpiredSignatureError:
            raise Exception("Token has expired")
        except jwt.InvalidTokenError:
            raise Exception("Invalid token")
        
        
    
        
        