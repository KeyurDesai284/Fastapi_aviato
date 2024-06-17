from fastapi import Depends,HTTPException,APIRouter
from sqlalchemy.orm import Session
from models.page_2 import Page2User
from schemas.page_2 import User2Create, User2Response
from config.db import get_db

router = APIRouter()

@router.post("/add_users",response_model=User2Response)
def create_user(user:User2Create, db: Session = Depends(get_db)):
    db_user = Page2User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/get_users/{user_id}", response_model=User2Response)
def get_user(user_id:int, db: Session = Depends(get_db)):
    user = db.query(Page2User).filter(Page2User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    return user

@router.patch("/update_users/{user_id}", response_model=User2Response)
def update_user(user_id: int, updated_data: User2Create, db: Session = Depends(get_db)):
    user = db.query(Page2User).filter(Page2User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    for key,value in updated_data.model_dump().items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

@router.delete("/delete_users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Page2User).filter(Page2User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    db.delete(user)
    db.commit()
    return {"detail": "User Deleted"}