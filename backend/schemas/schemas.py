from pydantic import BaseModel

# For use with Cognito
class User(BaseModel):
    username: str
    email: str
    password: str
