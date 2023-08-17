from sqlalchemy import Column, String, Integer, Float
from models import Base

class Produto(Base):
    __tablename__='produto'
    
    id=Column(Integer, primary_key = True, autoincrement=True) 
    nome=Column(String(15), default='Orquidea') 
    tipo=Column(String(15), nullable=True)
    cor=Column(String(15))
    tamanho=Column(String(1))
    quantidade=Column(Integer)
    valor=Column(Float)

    def __init__(self, nome:str, tipo:str, cor:str, tamanho:str, quantidade:int, valor:float):
        self.nome=nome
        self.tipo=tipo
        self.cor=cor
        self.tamanho=tamanho
        self.quantidade=quantidade
        self.valor=valor

