from fastapi import APIRouter, Depends, HTTPException
from dependences import pegar_sessao
from models import user
from sqlalchemy.orm import Session
from security import hash_password
from pydantic import BaseModel
from schemas import usuarioSchema



auth_router = APIRouter (prefix="/auth", tags=["auth"])

class UserCreate(BaseModel):
    nome: str
    email: str
    senha: str

@auth_router.get("/")
def home():
    return {"mensagem": "Essa é a rota base de autenticação"}


@auth_router.post("/criar-user")
def criar_user(usuario_schema: usuarioSchema, session: Session = Depends(pegar_sessao)):

    #consultar se ja existe um usuarui com o email digitado
    usuario = session.query(user).filter(user.email == usuario_schema.email). first()
    if usuario:
        raise HTTPException(status_code=400, detail="Ja existe um usuario com esse email")

    else:
        #bcrypt tem um limite de 72 caracteres, entao a senha é cortada para esse limite antes de ser criptografada
        senha_criptografada = hash_password(usuario_schema.senha) 

        novo_usuario = user(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.admin)

        session.add(novo_usuario)
        session.commit()

        raise HTTPException(status_code=200, detail="Novo usuario cadastrado com sucesso")
    
