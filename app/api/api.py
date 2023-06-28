from app.db.models import *
from app.db.db_caller import call_sp


def user_info(user_id: str):
    return call_sp('sp_get_users', user_id)


def user_register(username, company, email, password):
    return call_sp('sp_register', email, username, company, password)
