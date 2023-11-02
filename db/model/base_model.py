from db import DBConnector


class BaseModel(DBConnector):
    """
    Model básico, com inicialização de DBConnector
    """

    def __init__(self):
        self.metadata.create_all(DBConnector.get_engine())
        super().__init__()

    @classmethod
    def get_by_id(cls, id):
        try:
            with cls.get_session as session:
                return session.query(cls).filter(cls.id == id).first()
        except Exception as e:
            raise ModelException(f'Falha ao buscar por ID. {str(e)}')
    
    def save(self):
        try:
            # with self.get_session as session:
            with DBConnector.get_session() as session:
                session.add(self)
        except Exception as e:
            raise ModelException(f'Falha ao salvar objeto. {str(e)}')

    def to_dict(self) -> dict:
        """
        Conversão para dict. Necessário para transformar em json
        :return: dict
        """
        try:
            data = self.__dict__
            if '_sa_instance_state' in data:
                del data['_sa_instance_state']
            return data
        except Exception as e:
            raise ModelException(f'Falha ao converter objeto para dict {str(e)}')

    def from_dict(self, dict):
        """
        Conversão de dict para campos do objeto.
        :param dict:
        :return: None
        """
        try:
            self.__dict__ = dict
        except Exception as e:
            raise ModelException(f'Falha ao converter dict para campos de objeto {str(e)}')


class ModelException(Exception):
    """
    Exceção do módulo de Modelos
    """

    def __init__(self, message):
        self.message = message