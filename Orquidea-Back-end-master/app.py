from flask_openapi3 import OpenAPI, Info, Tag
from flask import request, redirect
from sqlalchemy.exc import IntegrityError
from schemas import (
    apresenta_produtos,
    apresenta_produto,
    ListagemProdutosSchema,
    ProdutoSchema,
    ProdutoViewSchema,
    ErrorSchema
)
from models import Produto, Session
from flask_cors import CORS


info = Info(title="OrquídeaAPI", version="1.2.0")

app = OpenAPI(__name__, info=info)

CORS(app)


# Tags da documentação
home_tag = Tag(
    name="Documentação",
    description="Documentação da aplicação"
)

produto_tag = Tag(
    name="Produto",
    description="Adição, visualização e remoção de produtos"
)


# DOCUMENTAÇÃO
@app.get("/", tags=[home_tag])
def home():
    """Documentação da API"""
    return redirect("/openapi")


# LISTAR PRODUTOS
@app.get(
    "/produtos",
    tags=[produto_tag],
    responses={
        "200": ListagemProdutosSchema,
        "404": ErrorSchema
    }
)
def get_produtos():
    """Lista todos os produtos cadastrados"""

    session = Session()

    try:
        produtos = session.query(Produto).all()

        return apresenta_produtos(produtos), 200

    finally:
        session.close()


# CADASTRAR PRODUTO
@app.post(
    "/produtos",
    tags=[produto_tag],
    responses={
        "200": ProdutoViewSchema,
        "409": ErrorSchema
    }
)
def create():
    """Cadastra um novo produto"""

    session = Session()

    try:
        data = ProdutoSchema.parse_obj(request.get_json())

        produto = Produto(
            nome=data.nome,
            tipo=data.tipo,
            cor=data.cor,
            tamanho=data.tamanho,
            quantidade=data.quantidade,
            valor=data.valor
        )

        session.add(produto)
        session.commit()

        return apresenta_produto(produto), 200

    except IntegrityError:
        session.rollback()

        return {
            "Erro": "Produto já cadastrado"
        }, 409

    except Exception:
        session.rollback()

        return {
            "Erro": "Erro de cadastro de produto"
        }, 400

    finally:
        session.close()


# DELETAR PRODUTO
@app.delete(
    "/produtos/<int:id>",
    tags=[produto_tag],
    responses={
        "200": ProdutoViewSchema,
        "404": ErrorSchema
    }
)
def delete(id):
    """Remove um produto pelo ID"""

    session = Session()

    try:
        produto = (
            session
            .query(Produto)
            .filter(Produto.id == id)
            .first()
        )

        if not produto:
            return {
                "Erro": "Produto não encontrado"
            }, 404

        session.delete(produto)
        session.commit()

        return {
            "Mensagem": "Produto excluído com sucesso"
        }, 200

    except Exception:
        session.rollback()

        return {
            "Erro": "Erro ao deletar produto"
        }, 400

    finally:
        session.close()


if __name__ == "__main__":
    app.run(debug=True)