from app.schemas.users import CreateUser


def create_user(user: CreateUser):
    user = user.model_dump()
    return{"success": True,
           "user": user}