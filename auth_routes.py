from fastapi import APIRouter, Depends, HTTPException
from dependences import pegar_sessao
from models import user
from sqlalchemy.orm import Session



auth_router = APIRouter (prefix="/auth", tags=["auth"])



@auth_router.get("/")
def home():
    return {"mensagem": "Essa é a rota base de autenticação"}


@auth_router.post("/auth/criar-user")
def criar_user(nome, senha, email, session: Session = Depends(pegar_sessao)):

    #consultar se ja existe um usuarui com o email digitado
    usuario = session.query(user).filter(user.email == email). first()
    if usuario:
        raise HTTPException(status_code=400, detail="Ja existe um usuario com esse email")

    else:

        novo_usuario = user(nome, email, senha)

        session.add(novo_usuario)
        session.commit()

        raise HTTPException(status_code=200, detail="Novo usuario cadastrado com sucesso")
    
