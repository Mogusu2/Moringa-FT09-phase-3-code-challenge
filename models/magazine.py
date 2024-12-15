from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    @staticmethod
    def create(name, category):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (name, category))
        conn.commit()
        conn.close()
        print(f"Magazine '{name}' created successfully!")

    @staticmethod
    def read_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM magazines')
        rows = cursor.fetchall()
        conn.close()
        return [Magazine(row['id'], row['name'], row['category']) for row in rows]

    @staticmethod
    def get_magazine_by_id(magazine_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM magazines WHERE id = ?', (magazine_id,))
        row = cursor.fetchone()
        conn.close()
        return Magazine(row['id'], row['name'], row['category']) if row else None
