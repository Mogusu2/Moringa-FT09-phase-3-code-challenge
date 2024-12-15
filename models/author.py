from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def create(name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
        print(f"Author '{name}' created successfully!")

    @staticmethod
    def read_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors')
        rows = cursor.fetchall()
        conn.close()
        return [Author(row['id'], row['name']) for row in rows]

    @staticmethod
    def get_author_by_id(author_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors WHERE id = ?', (author_id,))
        row = cursor.fetchone()
        conn.close()
        return Author(row['id'], row['name']) if row else None
