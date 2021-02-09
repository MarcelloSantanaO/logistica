from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class Session:
    def __init__(self):
        connector = 'postgresql'
        host = 'pgsql08-farm15.uni5.net'
        user = 'topskills14'
        password = 'olist21'
        dbname = 'topskills14'
        self.__conn_string = f'{connector}://{user}:{password}@{host}:5432/{dbname}'

    def __enter__(self):
        self.__engine = create_engine(self.__conn_string)
        Session = sessionmaker(self.__engine)
        self.__session = Session()
        return self.__session

    def __exit__(self, type, value, traceback):
        self.__engine.dispose()
        self.__session.close()
