import jaydebeapi as HSQL_
from datetime import datetime

class Connection:
    
    errCheck = False
    errMsg = ""

    UserName = "sa"
    Password = ""
    Java_Class = "org.hsqldb.jdbcDriver"
    conn = None

    def __init__(self, path):
        self.path = path
        self.HSQL_Driver_Path = f"{path}/hsqldb.jar"
        self.Database = f"jdbc:hsqldb:{path}/tmbulletin"
        self.conn = HSQL_.connect(self.Java_Class,self.Database,[self.UserName,self.Password],jars=self.HSQL_Driver_Path)
        self.cursor = self.conn.cursor()
        
    def clearErr(self):
        self.errCheck = False
        self.errMsg = ""

    def query(self, query, params=None):
        try:
            if params is not None:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            return self.cursor.fetchone()
        except Exception as Hata:
            if str(Hata).find("UNIQUE") != -1:
                self.errCheck = True
                self.errMsg = "Bu kullanıcı adı zaten kullanılıyor."

            else:
                with open("log.txt", "a") as log:
                    log.writelines(str(datetime.now()) + ": " + str(Hata) + "\n")
                self.errMsg ="Conn_errMsg", "Beklenmedik bir hata oluştu."
            return None

    def querys(self, query, params=None):
        try:
            if params is not None:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            return self.cursor.fetchall()
        except Exception as Hata:
            with open("log.txt", "a") as log:
                log.writelines(str(datetime.now()) + ": " + str(Hata) + "\n")
            return None

    def querymany(self, query, params=None):
        try:
            self.cursor.executemany(query, params)
            self.conn.commit()
            return self.cursor.fetchall()
        except Exception as Hata:
            with open("log.txt", "a") as log:
                log.writelines(str(datetime.now()) + ": " + str(Hata) + "\n")
            return None

    def close(self):
        self.conn.close()

    def __del__(self):
        self.conn.close()