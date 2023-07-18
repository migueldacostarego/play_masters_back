from app.db.db_caller import call_sp, call_sp_create


def user_info(user_id: str):
    return 0


def user_login(email: str, password: str):
    print(email, password)
    return 0


def user_games(user_id: str):
    return 0


def user_game_info(user_id: str, game_id: str):
    return 0


def user_register(username, company, email, password):
    return 0


def user_reset_password():
    return 0


def user_forgot_password(email: str):
    return 0


def user_change_password():
    return 0


def user_ban():
    return 0


def user_delete():
    return 0
