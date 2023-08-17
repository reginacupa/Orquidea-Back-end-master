from flask_openapi3 import OpenAPI, Info, Tag
from flask import Flask, request, jsonify, redirect
from sqlalchemy.exc import IntegrityError
from schemas import * 
from models import Produto, Session
from flask_cors import CORS

info = Info(title='OrquídeaAPI', version='1.0.0')
app = OpenAPI(__name__, info=info)
CORS (app)
doc_tag=Tag(name='Documentação', description= 'Descrição da Aplicaçao')

buy_tag=Tag(name='Buyrotas', description= 'Venda de orquídeas')

@app.get('/', tags=[doc_tag])
def index(): 
    """Documentação"""
    return redirect('openapi')

@app.get('/list', tags=[buy_tag])
def list():
    """Lista de Produtos"""
    session=Session()
    produtos=session.query(Produto).all()
    return apresenta_produtos(produtos)


@app.post('/create', tags=[buy_tag])
def create():
    """Cadastrar de Produtos"""
    try:
        data=ProdutoSchema.parse_obj(request.get_json())
        produto=Produto(
            nome=data.nome,
            tipo=data.tipo,
            cor=data.cor,
            tamanho=data.tamanho,
            quantidade=data.quantidade,
            valor=data.valor           
        )
        session=Session()
        session.add(produto) 
        session.commit()  
        return apresenta_produto(produto), 200 
    except Exception as e:
        return {"Erro": "Erro de cadastro de produto"}, 400
    
    except IntegrityError as e: 
        return {"Erro": "Produto já cadastrado"}, 409
    
@app.delete('/delete/<int:id>', tags=[buy_tag])
def delete(): 
    """Deletar Produtos"""
    id_produto=request.view_args.get('id')

    try:
        session=Session()
        count=session.query(Produto).filter(Produto.id==id_produto).delete()
        session.commit()
        if count: 
            return{"Menssagem":"Produto excluído com sucesso"}, 200
        else:
            return{"Erro":"Produto não encontrado"}, 404
    except Exception as e:
        return {"Erro": "Erro ao deletar produto"}, 400
    
    
if __name__ == '__main__':
    app.run()
    
