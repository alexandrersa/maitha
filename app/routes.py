from fastapi import APIRouter
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, RequestAgenda

import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def get_contatos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _contatos = crud.get_contatos(db=db, skip=skip, limit=limit)
    return Response(
        status="Ok", code="200", message="Dados obtidos com sucesso", result=_contatos
    )


@router.get("{id}")
async def get_contato(request: RequestAgenda, db: Session = Depends(get_db)):
    _contatos = crud.get_contato_by_id(db=db, id=request.parameter.id)

    return Response(
        status="Ok",
        code="200",
        message="Dados obtidos com sucesso",
        result=_contatos,
    )


@router.post("/")
async def create_contato_service(request: RequestAgenda, db: Session = Depends(get_db)):
    crud.create_contato(db, agenda=request.parameter)
    return Response(
        status="Ok", code="200", message="Contato adicionado com sucesso"
    ).dict(exclude_none=True)


@router.patch("{id}")
async def update_contato(request: RequestAgenda, db: Session = Depends(get_db)):
    _contatos = crud.update_contato(
        db=db,
        id=request.parameter.id,
        nome=request.parameter.nome,
        telefone=request.parameter.telefone,
    )
    return Response(
        status="Ok",
        code="200",
        message="Dados atualizados com sucesso",
        result=_contatos,
    )


@router.delete("{id}")
async def delete_contato(request: RequestAgenda, db: Session = Depends(get_db)):
    crud.remove_contato(db, id=request.parameter.id)
    return Response(
        status="Ok", code="200", message="Dados removidos com sucesso."
    ).dict(exclude_none=True)
