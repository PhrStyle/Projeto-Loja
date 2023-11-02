from datetime import date
from hashlib import md5

from sqlalchemy import Column, BigInteger, String, DateTime, Boolean, BLOB, SmallInteger, Date, desc, asc, ForeignKey, \
    REAL, FLOAT
from sqlalchemy.orm import relationship
from db import DBConnector
from db.model import BaseModel
from sqlalchemy.orm.decl_api import DeclarativeMeta


class Produtos(BaseModel, DBConnector.get_base_model()):

    __tablename__ = 'produtos'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    descricao = Column(String(128), nullable=False)
    valor = Column(FLOAT, nullable=False)

    def __init__(self):
        super().__init__()

    @classmethod
    def clear_produtos(cls):
        """
        Deleta todos os produtos
        """
        with DBConnector.get_session() as session:
            return session.query(Produtos).delete()

    @classmethod
    def get_all_produtos(cls):
        """
        Busca todas as empresas sem filtros
        """
        with DBConnector.get_session() as session:
            ret = session.query(Produtos).all()
            session.commit()
            session.close()
            return ret

    @classmethod
    def get_produto_by_id(cls, id):
        """
        Busca todas as empresas sem filtros
        """
        with DBConnector.get_session() as session:
            return session.query(Produtos).filter(Produtos.id == id).first()

    @classmethod
    def save_produto(cls, id, descricao, valor):
        """
        Cria um novo produto
        """
        with DBConnector.get_session() as session:
            try:
                produto = Produtos()
                produto.id = id
                produto.descricao = descricao
                produto.valor = valor
                session.add(produto)
                session.commit()
                session.close()
            except Exception as e:
                session.rollback()
                session.close()
                print(e)