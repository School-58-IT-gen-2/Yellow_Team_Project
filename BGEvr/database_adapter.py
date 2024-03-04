import psycopg2
class Adapter():

    def __init__(self, host, port, sslmode, dbname, user, password, target_session_attrs):
        self.host=host
        self.port=port
        self.sslmode=sslmode
        self.dbname=dbname
        self.user=user
        self.password=password
        self.target_session_attrs=target_session_attrs
        self.conn = None
        self.cursor = None
        
    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                sslmode=self.sslmode,
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                target_session_attrs=self.target_session_attrs
            )
            self.cursor = self.conn.cursor()
        except Exception as error:
            print(f'connection error:{error}')

    def select(self, table):
        request = f'SELECT * FROM "Yellow_team_project"."{table}"'
        self.cursor.execute(request)
        data = self.cursor.fetchall()
        return data
    
    def update(self, table, request, id):
        request_update = f'UPDATE "Yellow_team_project"."{table}" SET {request} WHERE id={id}'
        self.cursor.execute(request_update)
        self.conn.commit()

    def insert(self, table, collumns, values):
        request_insert = f'INSERT INTO "Yellow_team_project"."{table}" ({collumns}) VALUES ({values})'
        self.cursor.execute(request_insert)
        self.conn.commit()




db = Adapter(host="rc1d-9cjee2y71olglqhg.mdb.yandexcloud.net",port="6432",sslmode="verify-full",dbname="sch58_db",user="Admin",password="atdhfkm2024",target_session_attrs="read-write")
db.connect()
houses_data = db.select("houses")
print(houses_data)