from sqlalchemy import create_engine
from sqlalchemy import exc
from sqlalchemy import inspect
from sqlalchemy import text
import requests
from requests import Session
from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
import json
import datetime


# Postgres DB Connection
db_name = 'erp_dev'
db_user = 'psqladmin@erp-dev-db-server'
db_pass = 'Hhw5u3N9kQJ7'
db_host = 'erp-dev-db-server.postgres.database.azure.com' #'172.17.0.2' 
db_port = '5432'

# Connect to DB
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)

# API Connection
user = 'erp_integration_user'
password = '27uw9pjH0376BjMa'
rest_api_url = 'https://emgy-dev1.fa.em4.oraclecloud.com/fscmRestApi/resources/11.13.18.05/finBusinessUnitsLOV'


def test_connection():
    try:
        query = "" + \
                "SELECT * " + \
                "FROM psgerpext.xxcld_lockbox_format " + \
                "LIMIT 1"

        result_set = db.execute(query)
        return True
    except exc.SQLAlchemyError:
        print('problema de conexión con la base de datos')
        return False

def insert_header(file_name):
    try:
        # Retrieve the last number inserted inside the 'numbers'
        date_now = date.today()
        # print(str(date_now.strftime("%d/%m/%Y")))
        query = "" + \
                "INSERT INTO psgerpext.xxcld_header (country,name,file_name,file_date,status) " + \
                "VALUES('PT','Transfer','" + file_name[0:30] + "',to_date('" + str(date_now.strftime("%d/%m/%Y")) + "','dd/mm/yyyy'),'Pending') "
        result_set = db.execute(query)
        return True
    except exc.SQLAlchemyError:
        pass  # do something intelligent here



if __name__ == '__main__':
    """Programa Dummy"""

    print('Main: Application started')
    
    if test_connection():
        print('  Main: Reading File',"Prueba")

        try:
            payload = { }
            api_response = ''
            # Comentado para pruebas
            api_response = requests.get(rest_api_url, data=json.dumps(payload),
                                         auth=HTTPBasicAuth(user, password),
                                         headers={"Content-Type": "application/json"})

            insert_header(api_response)

        except IOError:
            print("Could not insert file:", "Prueba")


    print('Main: Application ended')
