import psycopg2
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
        request_update = f"""UPDATE "{self.schema_name}"."{table}" SET {request} WHERE id={id}"""
        self.cursor.execute(request_update)
        self.conn.commit()

    def insert(self, table, data):
        request_insert = f"""INSERT INTO "{self.schema_name}"."{table}" ({",".join(list(data.keys()))}) VALUES ({",".join(list(data.items()))})"""
        self.cursor.execute(request_insert)
        self.conn.commit()

    def insert_batch(self,table,data):
        for row in data:
            for key, value in row.items():
                if isinstance(row[key], int):
                    row[key] = str(row[key])
                elif isinstance(row[key], str):
                    row[key] = f"'{row[key]}'"

        for i in range(len(data)):
            names = f'"{'","'.join(list(data[i].keys()))}"'
            request_insert = f"""INSERT INTO "{self.schema_name}"."{table}" ({names}) VALUES ({",".join(list(data[i].values()))})"""
            print(request_insert)
            self.cursor.execute(request_insert)
        self.conn.commit()


    def delete(self,table,id):
        request_delete = f"""DELETE FROM "{self.schema_name}"."{table}" WHERE id = {id}"""
        self.cursor.execute(request_delete)
        self.conn.commit()


def get_csv():
    """должно быть что-то типо [{},{},...{}]"""
    f = open("cruisers.csv")
    res = []
    #d = f.read().split("\n")
    #print(d)
    arr_keys = f.readline().split(',')
    all_data = f.readlines()
    for i in range(len(all_data)):
        data = all_data[i].split(',')
        data_row_dict = {arr_keys[j].replace("\n",""): data[j].replace("\n","") for j in range(len(arr_keys))}
        res.append(data_row_dict)
    for j in range(len(res)):
        for k,v in res[j].items():
            try:
                res[j][k] = int(res[j][k])
            except:
                pass
    return res
            





db = Adapter(schema_name="Galactic Empire",host="rc1d-9cjee2y71olglqhg.mdb.yandexcloud.net",port="6432",dbname="sch58_db",sslmode=None,user="Admin",password="atdhfkm2024",target_session_attrs="read-write")
db.connect()

data = get_csv()
print(data)
db.insert_batch(table="Cruisers",data=data)