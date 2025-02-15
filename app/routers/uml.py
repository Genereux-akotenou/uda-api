from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..datastruct import models, database
from ..schemas import schemas
from ..repository import uml as umlRepository

router = APIRouter(
    prefix='/uml',
    tags=['UML/web']
)

@router.post('/class-diagram-xml',  status_code=200, response_model=schemas.ShowUMLSchema)
def class_diagram(request: schemas.UMLText):
    return umlRepository.toClassDigramXML(request)

@router.post('/class-diagram-obj',  status_code=200)
def class_diagram(request: schemas.UMLText):
    return umlRepository.toClassDigramOBJ(request)

@router.post('/atomic-sentence-maker',  status_code=200)
def class_diagram(request: schemas.UMLText):
    return umlRepository.sentenceSplit(request)

@router.post('/sentences-tokenizer',  status_code=200)
def class_diagram(request: schemas.UMLText):
    return umlRepository.stanzaPipeline(request)
