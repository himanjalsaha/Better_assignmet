from typing import Dict

class UserModel:
    def __init__(self, user_id: int, username: str, email: str, password: str):
        self.id = user_id
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self) -> Dict[str, str]:
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
