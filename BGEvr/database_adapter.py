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
        request = f'SELECT * FROM "Galactic Empire"."{table}"'
        self.cursor.execute(request)
        data = self.cursor.fetchall()
        return data
    
    def select_task_1(self):
        request = f'SELECT * FROM "Galactic Empire"."Cruisers"'
        self.cursor.execute(request)
        data = self.cursor.fetchall()
        return data

    def select_task_2(self):
        request = f"""SELECT * FROM "Galactic Empire"."Systems" as sys WHERE sys."Allegiance" = 'Empire' ORDER BY id ASC"""
        self.cursor.execute(request)
        data = self.cursor.fetchall()
        return data
    
    def select_task_3(self):
        request = """SELECT * FROM "Galactic Empire"."Planets" as pl WHERE pl."Name" != 'Mityas_planet' AND pl."Population" > 50 ORDER BY pl."Position" ASC;"""
        self.cursor.execute(request)
        data = self.cursor.fetchall()
        return data
    
    def select_task_4(self):
        request = """SELECT * FROM "Galactic Empire"."Planets" as pl WHERE pl."Name" != 'Mityas_planet' AND lower(pl."Name") = pl."Name" AND pl."Population" > 50 ORDER BY pl."Position" ASC;"""
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




db = Adapter(host="rc1d-9cjee2y71olglqhg.mdb.yandexcloud.net",port="6432",dbname="sch58_db",sslmode=None,user="Admin",password="atdhfkm2024",target_session_attrs="read-write")
db.connect()
lvl1 = db.select_task_1()
lvl2 = db.select_task_2()
lvl3 = db.select_task_3()
lvl4 = db.select_task_4()

print(lvl1,"\n",lvl2,"\n",lvl3,'\n',lvl4)