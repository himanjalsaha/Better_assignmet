
from flask import Blueprint
from controllers.users_controller import user_controller

users_bp = Blueprint("users", __name__)

users_bp.route("/users", methods=["GET"])(user_controller.get_users)
users_bp.route("/users", methods=["POST"])(user_controller.add_user)
users_bp.route("/users/login", methods=["POST"])(user_controller.login)