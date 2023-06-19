from sqlalchemy.orm import Session
from models import Agenda
from schemas import AgendaSchema


def get_contatos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Agenda).offset(skip).limit(limit).all()


def get_contato_by_id(db: Session, id: int):
    return db.query(Agenda).filter(Agenda.id == id).first()


def create_contato(db: Session, agenda: AgendaSchema):
    _contato = Agenda(nome=agenda.nome, telefone=agenda.telefone)
    db.add(_contato)
    db.commit()
    db.refresh(_contato)
    return _contato


def remove_contato(db: Session, id: int):
    _contato = get_contato_by_id(db=db, id=id)
    db.delete(_contato)
    db.commit()


def update_contato(db: Session, id: int, nome: str, telefone: str):
    _contato = get_contato_by_id(db=db, id=id)

    _contato.nome = nome
    _contato.telefone = telefone

    db.commit()
    db.refresh(_contato)
    return _contato
