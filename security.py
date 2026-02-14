from passlib.context import CryptContext

#CryptContext é o “gerenciador” de algoritmos de hash.
#Ele organiza como as senhas serão criptografadas e verificadas.
pwd_context = CryptContext(schemes=["bcrypt"], 
                           deprecated="auto")

def hash_password(password: str) -> str:
    #hash_password recebe uma senha em texto puro e retorna a versão criptografada.
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

