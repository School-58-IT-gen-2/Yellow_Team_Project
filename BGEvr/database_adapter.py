import psycopg2
import random
class Adapter():

    def __init__(self, host, port, sslmode, dbname,schema_name, user, password, target_session_attrs):
        self.host=host
        self.port=port
        self.sslmode=sslmode
        self.dbname=dbname
        self.user=user
        self.password=password
        self.target_session_attrs=target_session_attrs
        self.conn = None
        self.cursor = None
        self.schema_name = schema_name
        
    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                #sslmode=self.sslmode,
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                target_session_attrs=self.target_session_attrs,
                #sslcert = open("cert.crt")
            )
            self.cursor = self.conn.cursor()
        except Exception as error:
            print(f'connection error:{error}')

    def select(self, table):
        request = f"""SELECT * FROM "{self.schema_name}"."{table}" """
        self.cursor.execute(request)
        data = self.cursor.fetchall()
        return data
    
    def update(self, table, request, id):
        request_update = f"""UPDATE "{self.schema_name}"."{table}" SET {request} WHERE user_id={id}"""
        self.cursor.execute(request_update)
        self.conn.commit()

    def insert(self, table, data):
        request_insert = f"""INSERT INTO "{self.schema_name}"."{table}" ({",".join(list(data.keys()))}) VALUES ({",".join(list(data.items()))})"""
        self.cursor.execute(request_insert)
        self.conn.commit()

    def insert_batch(self,table,data,id_name):
        for row in data:
            for key, value in row.items():
                if isinstance(row[key], int):
                    row[key] = str(row[key])
                elif isinstance(row[key], str):
                    row[key] = f"'{row[key]}'"

        for i in range(len(data)):
            names = f'"{'","'.join(list(data[i].keys()))}"'
            request_insert = f"""INSERT INTO "{self.schema_name}"."{table}" ({names}) VALUES ({",".join(list(data[i].values()))}) RETURNING {id_name} """
            print(request_insert)
            self.cursor.execute(request_insert)
        self.conn.commit()
        t = self.cursor.fetchall()
        return t


    def delete(self,table,id):
        request_delete = f"""DELETE FROM "{self.schema_name}"."{table}" WHERE user_id = {id}"""
        self.cursor.execute(request_delete)
        self.conn.commit()

    def delete_batch(self,table,list_id):
        for i in list_id:
            request_delete = f"""DELETE FROM "{self.schema_name}"."{table}" WHERE user_id = {i}"""
            self.cursor.execute(request_delete)
            print(request_delete)
        self.conn.commit()


