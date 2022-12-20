from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from typing import List
from models.users import table_users
from config.db import conn
from schemas.user import User

user = APIRouter()

@user.get('/', response_model=List[User], tags=['Users'])
def get_users():
    return conn.execute(table_users.select()).fetchall()

@user.post('/users', response_model=User, tags=['Users'])
def create_user(user: User):
    new_user = {
        'name': user.name,
        'email': user.email,
        'password': user.password
    }
    result = conn.execute(table_users.insert().values(new_user))
    print(result)
    return 'Hola Papá'

@user.get('/users/{id}', response_model=User, tags=['Users'])
def get_user_id(id:str):
    return conn.execute(table_users.select().where(table_users.c.id==id)).first()

@user.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Users'])
def delete_user(id:str):
    result = conn.execute(table_users.delete().where(table_users.c.id==id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put('/users/{id}', response_model=User, tags=['Users'])
def update_user(id:str, user:User):
    conn.execute(table_users.update().values(
                                             name=user.name,
                                             email=user.email,
                                             password=user.password
                                             ).where(table_users.c.id==id))
    return "Update"
