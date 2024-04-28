from pydantic import BaseModel
from typing import List
from datetime import date
from model.praia import Praia


class PraiaSchema(BaseModel):
    """ Define como uma nova praia a ser inserido deve ser representado
    """
    nome: str = "Barra da Tijuca"
    cep: int = "22630011"
    cidade: str = "Rio de Janeiro"
    uf: str = "RJ"
    tipo: str = "Plastico"
    data: date = date(2023, 1 ,1)


class PraiaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome da praia.
    """
    nome: str = "Barra da Tijuca"


class ListagemPraiasSchema(BaseModel):
    """ Define como uma listagem de praia será retornada.
    """
    praias: List[PraiaSchema]


def apresenta_praias(praias: List[Praia]):
    """ Retorna uma representação da praia seguindo o schema definido em
        PraiaViewSchema.
    """
    result = []
    for praia in praias:
        result.append({
            "nome": praia.nome,
            "cep": praia.cep,
            "cidade": praia.cidade,
            "uf": praia.uf,
            "tipo": praia.tipo,
            "data": praia.data,
        })

    return {"praias": result}


class PraiaViewSchema(BaseModel):
    """ Define como uma praia será retornada
    """
    id: int = 1
    nome: str = "Barra da Tijuca"
    cep: int = "22630011"
    cidade: str = "Rio de Janeiro"
    uf: str = "RJ"
    tipo: str = "Plastico"
    data: date = date(2023, 1 ,1)
    


class PraiaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_praia(praia: Praia):
    """ Retorna uma representação da praia seguindo o schema definido em
        PraiaViewSchema.
    """
    return {
        "id": praia.id,
        "nome": praia.nome,
        "cidade": praia.cidade,
        "uf": praia.uf,
        "cep": praia.cep,
        "tipo": praia.tipo,
        "data": praia.data,
    }

