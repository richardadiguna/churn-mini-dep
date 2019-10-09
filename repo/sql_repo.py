import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SQLRepo():
    def __init__(self):
        connection_data = {
            'dbname': 'predictive_db',
            'user': 'predictive_user',
            'password': 's4p^W4@5Yms59!3',
            'host': '192.168.50.131'
        }
        self.__connection_string = "mysql+mysqlconnector://{}:{}@{}/{}".format(
            connection_data['user'],
            connection_data['password'],
            connection_data['host'],
            connection_data['dbname']
        )

        self.sql_engine = create_engine(self.__connection_string, echo=True)

        Session = sessionmaker(bind=self.sql_engine)
        self.__session = Session()

    def get_session(self):
        return self.__session
