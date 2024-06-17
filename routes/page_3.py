from fastapi import Depends,HTTPException,APIRouter
from sqlalchemy.orm import Session
from models.page_3 import Page3User
from schemas.page_3 import User3Create, User3Response
from config.db import get_db

router = APIRouter()

@router.post("/add_users",response_model=User3Response)
def create_user(user:User3Create, db: Session = Depends(get_db)):
    db_user = Page3User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/get_users/{user_id}", response_model=User3Response)
def get_user(user_id:int, db: Session = Depends(get_db)):
    user = db.query(Page3User).filter(Page3User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    return user

@router.patch("/update_users/{user_id}", response_model=User3Response)
def update_user(user_id: int, updated_data: User3Create, db: Session = Depends(get_db)):
    user = db.query(Page3User).filter(Page3User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    for key,value in updated_data.model_dump().items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

@router.delete("/delete_users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Page3User).filter(Page3User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    db.delete(user)
    db.commit()
    return {"detail": "User Deleted"}