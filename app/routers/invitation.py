from fastapi import APIRouter, Depends, status, Response, BackgroundTasks
from sqlalchemy.orm import Session
from ..datastruct import models, database
from ..schemas import schemas
from ..repository import invitation as invitationRepo
from ..security import oauth2
from typing import List
from ..repository import mail


router = APIRouter(
    prefix='',
    tags=['Invitation']
)

@router.post('/invitation/user/accept/{token}', status_code=200, response_model=schemas.ShowResponse)
def accept(token: str, db: Session = Depends(database.get_db)):
    return invitationRepo.accept(token, db)

@router.delete('/invitation/user/reject/{token}', status_code=200, response_model=schemas.ShowResponse)
def reject_as_user(token: str, db: Session = Depends(database.get_db)):
    return invitationRepo.reject_as_user(token, db)

@router.post('/invitation/guest/accept/{token1}/{token2}', status_code=200, response_model=schemas.ShowResponse)
def signup_and_accept(request: schemas.User, token1: str, token2: str, db: Session = Depends(database.get_db)):
    return invitationRepo.signup_and_accept(request, token1, token2, db)

@router.post('/invitation/guest/reject/{token1}/{token2}', status_code=200, response_model=schemas.ShowResponse)
def reject_as_guest(token1: str, token2: str, db: Session = Depends(database.get_db)):
    return invitationRepo.reject_as_guest(token1, token2, db,)

