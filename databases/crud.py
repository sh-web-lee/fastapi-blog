from sqlalchemy.orm import Session

from databases import models, schemas


def get_user(db: Session, user: schemas.UserForm):
    data = db.query(models.User).filter(
        models.User.email == user.email,
        models.User.password == user.password,
        models.User.is_active == True
    ).first()
    if data is None: return
    return schemas.UserResp.from_orm(data)