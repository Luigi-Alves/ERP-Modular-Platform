from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from schemas import usuarioSchema

#carrega os arquivos do .env
load_dotenv()
#encotra a key e carrega ela
Key_crypt = os.getenv("Key_crypt")

#CryptContext é o “gerenciador” de algoritmos de hash.
#Ele organiza como as senhas serão criptografadas e verificadas.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(senha: str):
    #hash_password recebe uma senha em texto puro e retorna a versão criptografada.
    return pwd_context.hash(senha)

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)

