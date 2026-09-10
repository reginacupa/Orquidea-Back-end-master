from models import Produto, Session


produtos = [
    {
        "nome": "Orquidea",
        "tipo": "Purpurata",
        "cor": "Branca",
        "tamanho": "P",
        "valor": 70.00,
        "quantidade": 5
    },
    {
        "nome": "Orquidea",
        "tipo": "Negra",
        "cor": "Negra",
        "tamanho": "P",
        "valor": 56.90,
        "quantidade": 6
    },
    {
        "nome": "Orquidea",
        "tipo": "Vanilla",
        "cor": "Amarela",
        "tamanho": "P",
        "valor": 32.00,
        "quantidade": 9
    },
    {
        "nome": "Orquidea",
        "tipo": "Cattleya",
        "cor": "Laranja",
        "tamanho": "P",
        "valor": 45.00,
        "quantidade": 4
    },
    {
        "nome": "Orquidea",
        "tipo": "Phalaenopsis",
        "cor": "Amarela",
        "tamanho": "P",
        "valor": 159.90,
        "quantidade": 2
    },
    {
        "nome": "Orquidea",
        "tipo": "Oncidium",
        "cor": "Amarela",
        "tamanho": "P",
        "valor": 42.00,
        "quantidade": 3
    }
]


session = Session()

try:
    if session.query(Produto).count() > 0:
        print("Banco já possui produtos. Seed não executado.")

    else:
        for item in produtos:
            produto = Produto(**item)
            session.add(produto)

        session.commit()

        print("6 produtos cadastrados com sucesso! 🌸")

finally:
    session.close()