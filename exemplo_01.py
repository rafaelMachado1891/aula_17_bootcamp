from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

# Criando engine de conexão com SQLite
engine = create_engine("sqlite:///meu_banco.db", echo=True)

print('Conexão com SQLite estabelecida')

# Declarando a base
Base = declarative_base()

# Definindo a classe Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Criando a tabela no banco de dados
Base.metadata.create_all(engine)
