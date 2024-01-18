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
    def saveAdminInfo(name: str, pw: str):
        DB.openDB()
        cursor = DB.conn.cursor()

        try:
            cursor.execute('''CREATE TABLE Admin
                              (admin TEXT PRIMARY KEY, 
                                name TEXT,
                                password TEXT)''')
            cursor.execute("INSERT INTO Admin VALUES ( ?, ?, ?)", ("admin", name, pw,))
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
    def saveEmpInfo(UID: str, fName: str, mName: str, lName: str, phone: str, email: str, pos: str, f1: str, f2: str):
        DB.openDB()
        cursor = DB.conn.cursor()
        try:
            print(fName)
            cursor.execute(
                '''CREATE TABLE Employee (id TEXT PRIMARY KEY, fName TEXT, mName TEXT, lName TEXT, phone TEXT, email TEXT, pos TEXT)''')

            cursor.execute(
                '''CREATE TABLE Fingers (userID TEXT PRIMARY KEY, f1 TEXT, f2 TEXT)''')
            DB.conn.commit()
        except Error as e:
            print(e)
            pass
        try:
            cursor.execute("INSERT INTO Employee VALUES ( ?, ?, ?, ?, ? , ?, ?)",
                           (UID, fName, mName, lName, phone, email, pos,))

            cursor.execute("INSERT INTO Fingers VALUES ( ? , ?, ?)",
                           (UID, f1, f2,))
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
    def getEmpInfo(UID: str):
        DB.openDB()
        cursor = DB.conn.cursor()
        try:
            rows = cursor.execute("SELECT * FROM Employee WHERE id = ?", (UID,)).fetchone()
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
    def removeEmp(UID):
        DB.openDB()
        cursor = DB.conn.cursor()
        try:
            cursor.execute(f"DELETE FROM Employee WHERE id= {UID}")
            cursor.close()
            DB.closeDB()
            return True
        except Error as e:
            print(e)

            cursor.close()
            DB.closeDB()
            return False
        pass

    @staticmethod
    def getFingPrints():
        DB.openDB()
        cursor = DB.conn.cursor()
        try:
            rows = cursor.execute("SELECT * FROM Fingers").fetchall()
            print(rows)
        except Error as e:
            rows = [[]]

            print(e)

        cursor.close()
        DB.closeDB()
        return rows
        pass

    @staticmethod
    def saveEmpAttendance(empUsername: str, date: str, timeIn: str, timeOut: str):
        DB.openDB()
        cursor = DB.conn.cursor()

        try:
            cursor.execute(f'''CREATE TABLE {empUsername}
                                  (date TEXT PRIMARY KEY, 
                                    timeIn TEXT,
                                    timeOut TEXT)''')

            DB.conn.commit()
        except Error as e:
            print(e)
            pass
        try:
            cursor.execute(f"INSERT INTO {empUsername} VALUES ( ?, ?, ?)", (date, timeIn, timeOut,))
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
    def getEmpAttendance(empUsername: str):
        DB.openDB()
        cursor = DB.conn.cursor()
        try:
            rows = cursor.execute(f"SELECT * FROM {empUsername}").fetchall()
            print(rows)
        except Error as e:
            rows = [[]]

            print(e)

        cursor.close()
        DB.closeDB()
        return rows
        pass

