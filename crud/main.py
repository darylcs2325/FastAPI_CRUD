from fastapi import FastAPI
from routers.users import user

app = FastAPI(
    title='Mi primer API',
    description= 'Este es mi primer API',
    version='0.0.1',
    openapi_tags=[{
        'name': 'Users',
        'description': 'Users Routers'
    }]
)

app.include_router(user)