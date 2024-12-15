from database.connection import get_db_connection

class Magazine:
    @staticmethod
    def create(name, category):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (name, category))
            conn.commit()
            return cursor.lastrowid
        finally:
            conn.close()

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM magazines')
            return cursor.fetchall()
        finally:
            conn.close()
