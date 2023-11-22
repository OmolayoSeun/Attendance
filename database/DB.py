import sqlite3
from sqlite3 import Error


class DB:

    conn = sqlite3.connect("data.db")

    @staticmethod
    def openDB():
        DB.conn = sqlite3.connect("data.db")

    @staticmethod
    def closeDB():
        DB.conn.close()

    @staticmethod
    def saveAdminInfo(name: str, biz: str, pw: str):
        DB.openDB()
        cursor = DB.conn.cursor()

        try:
            cursor.execute('''CREATE TABLE Admin
                              (admin TEXT PRIMARY KEY, 
                                name TEXT, 
                                biz TEXT,
                                password TEXT)''')
            cursor.execute("INSERT INTO Admin VALUES ( ?, ?, ?, ?)", ( "admin",name, biz, pw,))
            cursor.close()
            DB.conn.commit()
            DB.closeDB()
            return True
        except Error as e:
            cursor.close()
            DB.closeDB()
            return False


        pass

    @staticmethod
    def getAdminInfo():
        DB.openDB()
        cursor = DB.conn.cursor()
        try:
            rows = cursor.execute("SELECT * FROM Admin").fetchall()
        except Error as e:
            print(e)
            rows = [[]]
        print(rows)
        cursor.close()
        DB.closeDB()
        return rows[0]

    @staticmethod
    def saveEmpInfo(Eid: str, fName: str, mName: str, lName: str, phone: str, email: str, pos: str):
        DB.openDB()
        cursor = DB.conn.cursor()
        try:
            cursor.execute('''CREATE TABLE Employee (id TEXT PRIMARY KEY, fName TEXT, mName TEXT, lName TEXT, phone TEXT, email TEXT, pos TEXT)''')
            DB.conn.commit()
        except Error as e:
            print(e)
            pass
        try:
            cursor.execute("INSERT INTO Employee VALUES ( ?, ?, ?, ?, ? , ?, ?)", ( Eid, fName, mName, lName, phone, email, pos,))
            cursor.close()
            DB.conn.commit()
            DB.closeDB()
            return True
        except Error as e:
            print(e)
            cursor.close()
            DB.closeDB()
            return False
    pass

    @staticmethod
    def getEmpInfo(Eid: str):
        DB.openDB()
        cursor = DB.conn.cursor()
        try:
            rows = cursor.execute("SELECT * FROM Employee WHERE id = ?", (Eid,)).fetchone()
            print(rows)
        except Error as e:
            rows = [[]]
            print(e)

        cursor.close()
        DB.closeDB()
        return rows

    @staticmethod
    def getEmpList():
        DB.openDB()
        cursor = DB.conn.cursor()
        try:
            rows = cursor.execute("SELECT * FROM Employee").fetchall()
            print(rows)
        except Error as e:
            rows = [[]]
            print(e)

        cursor.close()
        DB.closeDB()
        return rows
        pass

    @staticmethod
    def changePassword():
        pass

    @staticmethod
    def removeEmp():
        pass

#
# #a = DB.saveAdminInfo("omo", "omo", "omo")
# #
# #
#
#a = DB.saveEmpInfo( "deal", "asa", "aa", "whseed", "gdg", "hhd", "sited")
#print(a)
#
#print(DB.getEmpInfo("deal"))
# DB.getAdminInfo()
#DB.getEmpList()
