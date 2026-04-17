from typing import Optional

from pydantic import BaseModel
from fastapi import FastAPI, status

app = FastAPI()


#
# # Pydantic Model
# class User(BaseModel):
#     name: str
#     age: int
#
#
# # POST (Create)
# @app.post("/users")
# def create_user(user: User):
#     return {
#         "message": "User created",
#         "data": User
#     }
#
#
# # Optional field
# class Users(BaseModel):
#     name: str
#     age: int
#     email: Optional[str] = None
#
#
# @app.put("/users/{user_id}")
# def update_user(user_id: int, users: Users):
#     return {
#         "id": user_id,
#         "updated_data": users,
#     }


# Path + Query + Body BIRGA
class UserCreate(BaseModel):
    name: str
    age: int


class UserResponse(BaseModel):
    id: int
    name: str
    age: int


@app.post("/users/{user_id}",
          response_model=UserResponse,
          status_code=status.HTTP_201_CREATED
          )
def create_user(user_id: int, user: UserCreate, active: bool = True):
    return {
        "id": user_id,
        "name": user.name,
        "age": user.age
    }
