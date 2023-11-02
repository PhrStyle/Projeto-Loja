import os
from dotenv import load_dotenv
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import NullPool


class DBConnector:
    """
    Classe de conexão ao banco de dados e criação de sessões.
    """
    __sessionmaker = None
    __engine = None
    __base = None

    def __init__(self):
        pass

    @classmethod
    @contextmanager
    def get_session(cls) -> Session:
        """
        Retorna uma sessão com o banco de dados gerenciada pelo contexto
        """
        if cls.__sessionmaker is None:
            cls.__config()
        session = cls.__sessionmaker()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise DBException(str(e))
        finally:
            session.close()

    @classmethod
    def get_engine(cls) -> Engine:
        """
        Retorna a engine de conexão ao banco de dados.
        """
        try:
            if cls.__engine is None:
                cls.__config()
            return cls.__engine
        except Exception as e:
            raise DBException(str(e))

    @classmethod
    def get_base_model(cls) -> object:
        """
        Retorna a BaseModel para instanciação de models de base declarativa.
        """
        try:
            if cls.__base is None:
                cls.__config()
            return cls.__base
        except Exception as e:
            raise DBException(str(e))

    @classmethod
    def __config(cls) -> None:
        """
        Configura o banco de dados.
        Precisa ser chamado apenas uma vez.
        """
        load_dotenv()
        url = f"{os.environ.get('DB_ENGINE')}://" \
              f"{os.environ.get('DB_USER')}:" \
              f"{os.environ.get('DB_PASS')}@" \
              f"{os.environ.get('DB_SERVER')}:" \
              f"{os.environ.get('DB_PORT')}/" \
              f"{os.environ.get('DB_NAME')}"
        try:
            cls.__engine = create_engine(
                url,
                poolclass=NullPool,
            )
            cls.__sessionmaker = sessionmaker(cls.__engine, expire_on_commit=False)
            cls.__base = declarative_base()
        except Exception as e:
            raise DBException(str(e))



class DBException(Exception):
    """
    Exceção do módulo de banco de dados
    """

    def __init__(self, message):
        self.message = message
