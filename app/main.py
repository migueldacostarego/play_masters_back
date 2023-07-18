from fastapi import FastAPI, Request, Depends
from fastapi.security import OAuth2PasswordBearer
from app.db.models import *
from app.api import api

app = FastAPI()


@app.get("/api/user/{user_id}/info")
def user_info(user_id):
    return api.user_info(user_id)


@app.get("/api/user/{user_id}/games")
def user_games(user_id):
    return {user_id}


@app.get("/api/user/{user_id}/games/{game_id}")
def user_game_info(user_id, game_id):
    return {user_id, game_id}


@app.get("/api/user/{email}/login/{password}")
def user_login(email, password):
    return api.user_login(email, password)


@app.post("/api/user/register", status_code=201)
def user_register(user_info: UserCreate):
    return api.user_register(user_info.username, user_info.company, user_info.email, user_info.password)


@app.post("/api/user/reset_password", status_code=201)
def user_reset_password(user_id: str):
    print(user_id)
    return


@app.post("/api/user/forgot_password", status_code=201)
def user_forgot_password(email: str):
    return


@app.put("/api/user/change_password")
def user_change_password(psw: str):
    return


@app.put("/api/user/ban")
def user_ban(user_id: str):
    return {}


@app.delete("/api/user/{user_id}/delete")
def user_delete(user_id: str):
    return {}
