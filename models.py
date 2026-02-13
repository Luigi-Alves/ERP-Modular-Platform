import uuid
from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID

#conexao banco de dados
db = create_engine("sqlite:///banco.db")

#base banco de dados
base = declarative_base()

class user(base):
    __tablename__ = "Users"

    id = Column(String, primary_key = True, default=lambda: str( uuid.uuid4()))
    nome = Column ("nome", String)
    email = Column ("email", String)
    senha = Column ("senha", String)
    admin = Column ("admin", Boolean, default= False)

    def __init__(self, nome, email, senha, admin= False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.admin = admin