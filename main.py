from datetime import datetime, timedelta
from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

# local
from databases import crud, models, schemas
from databases.connect import SessionLocal

from messages.mconfig import mconfigs
from messages.message import Message

from sys_config import sys_configs


web = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_jwt_token(data: dict, expire_delta=timedelta(minutes=sys_configs.ACCESS_TOKEN_EXPIRE_MINUTES)):
    end_time = datetime.utcnow() + expire_delta
    data.update({'exp': end_time})
    token = jwt.encode(claims=data, key=sys_configs.SECRET_KEY, algorithm=sys_configs.ALGORITHM)
    return token


async def auth_token(token = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token=token, key=sys_configs.SECRET_KEY, algorithms=sys_configs.ALGORITHM)
        name = payload.get('name')
        email = payload.get('email')
        return schemas.UserResp(email=email, name=name)
    except Exception as e:
        print(e)
        return None


@web.post('/u/login', response_model=None)
async def user_login(user: schemas.UserForm, db: Session = Depends(get_database)):
    u = crud.get_user(db, user=user)
    if u is None:
        resp = Message(code=mconfigs.c4001)
    else:
        resp = Message(code=mconfigs.c2001)
        resp.update('user', u)
        resp.update('token', create_jwt_token(u.dict()))
    return resp.to_dict()


@web.get('/test/token')
async def test_token(user=Depends(auth_token)):
    return user


if __name__=='__main__':
    import uvicorn
    uvicorn.run('main:web', reload=True, port=8000, host='0.0.0.0')
    #     192.168.10.40