from datetime import date
from hashlib import md5

from sqlalchemy import Column, BigInteger, String, DateTime, Boolean, BLOB
from sqlalchemy.orm import relationship
from db import DBConnector
from db.model import BaseModel
from sqlalchemy.orm.decl_api import DeclarativeMeta


class Usuarios(BaseModel, DBConnector.get_base_model()):

    __tablename__ = 'usuarios'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user = Column(String(128), nullable=False)
    senha = Column(String(128), nullable=False)

    def __init__(self):
        super().__init__()


    @classmethod
    def get_all(cls):
        """
        Busca todos os usuários sem user nenhum filtro
        """
        with DBConnector.get_session() as session:
            ret = session.query(Usuarios).order_by(Usuarios.user).all()
            session.commit()
            session.close()
            return ret

    @classmethod
    def get_by_id(cls, id):
        """
        Busca todos os usuários sem user nenhum filtro
        """
        with DBConnector.get_session() as session:
            ret = session.query(Usuarios).filter(Usuarios.id == id).first()
            session.commit()
            session.close()
            return ret

    @classmethod
    def get_user_by_user_and_psw(cls, user, senha):
        """
        Busca todas as empresas sem filtros
        """
        with DBConnector.get_session() as session:
            ret = session.query(Usuarios).filter(Usuarios.user == user) .filter(Usuarios.senha == md5(senha.encode()).hexdigest()).first()
            session.commit()
            session.close()
            return ret

    @classmethod
    def save_user(cls, user, senha, gerenciarusers, gerenciarproprio, veroutros, gerenciaroutros):
        """
        Busca uma empresa filtrando pelo id
        """
        with DBConnector.get_session() as session:
            try:
                usuario = Usuarios()
                usuario.user = user
                usuario.senha = md5(senha.encode()).hexdigest()
                usuario.gerenciarusers = gerenciarusers
                usuario.gerenciarproprio = gerenciarproprio
                usuario.veroutros = veroutros
                usuario.gerenciaroutros = gerenciaroutros
                session.add(usuario)
                session.commit()
                session.close()
            except Exception as e:
                session.rollback()
                session.close()
                print(e)

    @classmethod
    def get_usuario_by_user(cls, user):
        """
        Busca todas as contatos sem filtros
        """
        with DBConnector.get_session() as session:
            ret = session.query(Usuarios).filter(Usuarios.user == user).first()
            session.close()
            return ret

    @classmethod
    def atualizarsenha(cls, iduser, senha):
        """
        Atualiza a senha do usuário
        """
        with DBConnector.get_session() as session:
            try:
                usuario = session.query(Usuarios).filter(Usuarios.id == iduser).first()
                print(usuario)
                usuario.senha = md5(senha.encode()).hexdigest()
                session.commit()
                session.close()
            except Exception as e:
                session.rollback()
                print(e)

    @classmethod
    def delete_by_id(cls, id):
        """
        Exclui um grupo por id
        """
        with DBConnector.get_session() as session:
            try:
                session.query(Usuarios).filter(Usuarios.id == id).delete()
                session.commit()
                session.close()
            except Exception as e:
                print(e)