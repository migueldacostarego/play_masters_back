from app.db.db_caller import call_sp, call_sp_create


def user_info(user_id: str):
    return call_sp('sp_get_users', user_id)


def user_login(email: str, password: str):
    print(email, password)
    return call_sp('sp_login', email, password)


def user_games(user_id: str):
    return call_sp('', user_id)


def user_game_info(user_id: str, game_id: str):
    return call_sp('sp_getAllGamesAndBets', user_id, game_id)


def user_register(username, company, email, password):
    return call_sp_create('sp_register', email, username, company, password)


def user_reset_password():
    return call_sp('sp_reset_pwd')


def user_forgot_password(email: str):
    return call_sp('sp_forgot_pwd', email)


def user_change_password():
    return call_sp()


def user_ban():
    return call_sp()


def user_delete():
    return call_sp()
