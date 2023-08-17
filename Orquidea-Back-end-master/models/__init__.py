from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database 
import os

from models.base import Base
from models.produto1 import Produto
db_path='database/'
db_url = 'sqlite:///%s/db.sqlite3' % db_path

if not os.path.exists(db_path):
    os.makedirs(db_path)

engine = create_engine(db_url, echo=False);

Session = sessionmaker(bind=engine);

if not database_exists(db_url):
    create_database(db_url)

Base.metadata.create_all(engine);
session=Session()
itens=[ 
    {'nome': 'Orquidea', 'tipo': 'Purpurata', 'cor': 'Branca', 'tamanho': 'P', 'valor': 70.00, 'quantidade': 5},
    {'nome': 'Orquidea', 'tipo': 'Negra', 'cor': 'Negra', 'tamanho': 'P', 'valor': 56.90, 'quantidade': 6},
    {'nome': 'Orquidea', 'tipo': 'Vanilla', 'cor': 'Amarela', 'tamanho': 'P', 'valor': 32.00, 'quantidade': 9},
    {'nome': 'Orquidea', 'tipo': 'Cattleya', 'cor': 'Laranja', 'tamanho': 'P', 'valor': 45.00, 'quantidade': 4},
    {'nome': 'Orquidea', 'tipo': 'Phalaenopsis', 'cor': 'Amarela', 'tamanho': 'P', 'valor': 159.90, 'quantidade': 2},
    {'nome': 'Orquidea', 'tipo': 'Oncidium', 'cor': 'Amarela', 'tamanho': 'P', 'valor': 42.00, 'quantidade': 3}
]
for item in itens:
    novo_item=Produto(
        cor=item['cor'],
        nome=item['nome'],
        tamanho=item['tamanho'],
        quantidade=item['quantidade'],
        valor=item['valor'],
        tipo=item['tipo']
    )
    session.add(novo_item)
session.commit()

    





