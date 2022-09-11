from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

user_router = APIRouter(
    tags=["User"]
)

users = dict()

@user_router.post("/signup")
async def sign_new_user(data: User)->dict:
    if data.email in users:
         raise HTTPException(
             status_code= status.HTTP_409_CONFLICT,
             detail="User with supplied username exist"
         )
    users[data.email]= data
    
    return{
        "message": "User successfully registred!!!"
    }

@user_router.post("/signin")
async def sign_user_in(user:UserSignIn) ->dict:
    if users[user.email] not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user Not Found"
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong does not exist!!!!"
        )
    return {
        "message": "User signed successfully"
    }
    