from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from datetime import date
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Praia
from logger import logger
from schemas import *
from flask_cors import CORS
from flask import request

info = Info(title="API Guardians of Atlantis", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
praia_tag = Tag(name="Praia", description="Adição, visualização e remoção de praias à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/praia', tags=[praia_tag],
          responses={"200": PraiaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_praia(form: PraiaSchema):
    """Adiciona uma nova praia à base de dados

    Retorna uma representação das praia.
    """
    praia = Praia(
        nome=form.nome,
        cep = form.cep,
        cidade = form.cidade,
        uf = form.uf,
        tipo = form.tipo,
        data = form.data)
    logger.debug(f"Adicionando praia de nome: '{praia.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando praia
        session.add(praia)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado praia de nome: '{praia.nome}'")
        return apresenta_praia(praia), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Praia de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar praia '{praia.nome}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar praia '{praia.nome}', {error_msg}")
        return {"message": error_msg}, 400


@app.get('/praias', tags=[praia_tag],
         responses={"200": ListagemPraiasSchema, "404": ErrorSchema})
def get_praias():
    """Faz a busca por todas as praias cadastradas

    Retorna uma representação da listagem de praias.
    """
    logger.debug(f"Coletando praias ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    praias = session.query(Praia).all()

    if not praias:
        # se não há praias cadastrados
        return {"praias": []}, 200
    else:
        logger.debug(f"%d praias encontradas" % len(praias))
        # retorna a representação de praia
        print(praias)
        return apresenta_praias(praias), 200


@app.get('/praia', tags=[praia_tag],
         responses={"200": PraiaViewSchema, "404": ErrorSchema})
def get_praia(query: PraiaBuscaSchema):
    """Faz a busca por uma Praia a partir do nome da praia

    Retorna uma representação das praias.
    """
    praia_nome = query.nome
    logger.debug(f"Coletando dados sobre praia #{praia_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    praia = session.query(Praia).filter(Praia.nome == praia_nome).first()

    if not praia:
        # se o praia não foi encontrado
        error_msg = "Praia não encontrado na base :/"
        logger.warning(f"Erro ao buscar praia '{praia_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Praia encontrada: '{praia.nome}'")
        # retorna a representação de praia
        return apresenta_praia(praia), 200


@app.delete('/praia', tags=[praia_tag],
            responses={"200": PraiaDelSchema, "404": ErrorSchema})
def del_praia(query: PraiaBuscaSchema):
    """Deleta uma praia a partir do nome informado

    Retorna uma mensagem de confirmação da remoção.
    """
    praia_nome = unquote(unquote(query.nome))
    print(praia_nome)
    logger.debug(f"Deletando dados sobre praia #{praia_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Praia).filter(Praia.nome == praia_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletando praia #{praia_nome}")
        return {"message": "Praia removida", "id": praia_nome}
    else:
        # se a praia não foi encontrada
        error_msg = "Praia não encontrada na base :/"
        logger.warning(f"Erro ao deletar praia #'{praia_nome}', {error_msg}")
        return {"message": error_msg}, 404


@app.put('/praia', tags=[praia_tag],
          responses={"200": PraiaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def update_praia_type(form: PraiaSchema):
    """Alterar o tipo da praia no banco de dados.

    Retorna a praia.
    """
    praia_nome = form.nome  # Nome da praia
    new_type = form.tipo  # Novo tipo

    logger.debug(f"Tipo da praia '{praia_nome}' alterado para '{new_type}'")
    try:
        session = Session()
        praia = session.query(Praia).filter(Praia.nome == praia_nome).first()
        
        if not praia:
            return {"message": "Praia não encontrada"}, 404
        
        praia.tipo = new_type  # Atualiza o tipo da praia
        session.commit()
        
        logger.debug(f"Tipo da praia '{praia_nome}' alterado para '{new_type}'")
        return apresenta_praia(praia), 200

    except IntegrityError as e:
        error_msg = "Erro ao atualizar o tipo da praia"
        logger.warning(f"Erro ao atualizar o tipo da praia '{praia_nome}': {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Falha ao alterar o tipo da praia"
        logger.warning(f"Falha ao alterar o tipo da praia '{praia_nome}': {error_msg}")
        return {"message": error_msg}, 400
