from pydantic import BaseModel
from typing import Optional, List
from models.produto1 import Produto


class ProdutoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str = "Orquidea Purpurata"
    quantidade: Optional[int] = 145
    valor: float = 70.00
    tipo: str = "Purpurata"
    tamanho: str = "P"
    cor: str = "Branca"


class ProdutoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    nome: str = "Orquidea"


class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    produtos:List[ProdutoSchema]


def apresenta_produtos(produtos: List[Produto]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for produto in produtos:
        result.append({
            "id": produto.id,
            "nome": produto.nome,
            "quantidade": produto.quantidade,
            "valor": produto.valor,
            "tamanho":produto.tamanho,
            "cor":produto.cor,
            "tipo": produto.tipo,
        })

    return {"produtos": result}


class ProdutoViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    id: int = 1
    nome: str = "Orquidea"
    quantidade: Optional[int] = 1
    valor: float = 70,00
    cor: str = "Branca"
    tamanho: str = "P"
    tipo: str = "Purpurata"
    

class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_produto(produto: Produto):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": produto.id,
        "nome": produto.nome,
        "quantidade": produto.quantidade,
        "valor": produto.valor,
        "cor":produto.cor,
        "tamanho":produto.tamanho,
        "tipo":produto.tipo,
        
    }
