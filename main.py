from fastapi import FastAPI
from config import db
from config.db import Base, engine
from routes import page_1, page_2, page_3, email_invite

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(page_1.router, prefix="/page1")
app.include_router(page_2.router, prefix="/page2")
app.include_router(page_3.router, prefix="/page3")
app.include_router(email_invite.router, prefix="/invite")