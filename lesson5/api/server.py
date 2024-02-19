from fastapi import FastAPI
from .controllers import language_controller, phone_controller, user_controller, user_language_controller

app = FastAPI()
app.include_router(language_controller)
app.include_router(phone_controller)
app.include_router(user_controller)
app.include_router(user_language_controller)
