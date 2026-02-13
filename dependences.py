from sqlalchemy.orm import sessionmaker
from models import db


#abrir e fechar sessao do Banco de dados
def pegar_sessao():
    try:
        Session = sessionmaker(bind= db)
        session = Session()

        yield session

    finally:
        
        session.close()
    


