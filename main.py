from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session

from databases import crud, models, schemas
from databases.connect import SessionLocal


web = FastAPI()

def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@web.post('/u/login')
async def user_login(user: schemas.UserForm, db: Session = Depends(get_database)):
    return crud.get_user(db, user=user)


if __name__=='__main__':
    import uvicorn
    uvicorn.run('main:web', reload=True, port=8000, host='0.0.0.0')
    #     192.168.10.40