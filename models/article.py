from database.connection import get_db_connection

class Article:
    @staticmethod
    def create(title, content, author_id, magazine_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                (title, content, author_id, magazine_id)
            )
            conn.commit()
            return cursor.lastrowid
        finally:
            conn.close()

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM articles')
            return cursor.fetchall()
        finally:
            conn.close()

    @staticmethod
    def update_content(article_id, content):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('UPDATE articles SET content = ? WHERE id = ?', (content, article_id))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()

    @staticmethod
    def delete(article_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM articles WHERE id = ?', (article_id,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()

    @staticmethod
    def get_by_author(author_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                '''
                SELECT articles.title, magazines.name AS magazine_name
                FROM articles
                JOIN magazines ON articles.magazine_id = magazines.id
                WHERE articles.author_id = ?
                ''',
                (author_id,)
            )
            return cursor.fetchall()
        finally:
            conn.close()
