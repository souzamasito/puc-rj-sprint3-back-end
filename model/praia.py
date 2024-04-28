from sqlalchemy import Column, String, Integer, DateTime, Date
from datetime import datetime
from typing import Union

from  model import Base

class Praia(Base):
    __tablename__ = 'praia'

    id = Column("pk_praia", Integer, primary_key=True)
    nome = Column(String(80))
    cep = Column(Integer)
    cidade = Column(String(80))
    uf = Column(String(20))
    tipo = Column(String(30))
    data = Column(Date, )
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, cep:int, cidade:str, uf:str, tipo:str, data:Date,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um item praia

        Arguments:
            nome: nome da praia.
            cep: cep do local onde está o lixo
            cidade: cidade onde está a praia
            uf: Unidade de Federação da praia
            tipo: tipo de lixo
            data: data em que foi observado
            data_insercao: data de quando a informação foi inserida à base
        """
        self.nome = nome
        self.cep= cep
        self.cidade = cidade
        self.uf = uf
        self.tipo = tipo
        self.data = data
    

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

            


