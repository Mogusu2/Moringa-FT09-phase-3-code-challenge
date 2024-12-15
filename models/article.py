from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    @staticmethod
    def create(title, content, author_id, magazine_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
            (title, content, author_id, magazine_id),
        )
        conn.commit()
        conn.close()
        print(f"Article '{title}' created successfully!")

    @staticmethod
    def read_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles')
        rows = cursor.fetchall()
        conn.close()
        return [Article(row['id'], row['title'], row['content'], row['author_id'], row['magazine_id']) for row in rows]

    @staticmethod
    def update_content(article_id, new_content):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE articles SET content = ? WHERE id = ?',
            (new_content, article_id),
        )
        conn.commit()
        conn.close()
        print(f"Article ID {article_id} updated successfully!")

    @staticmethod
    def delete(article_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM articles WHERE id = ?', (article_id,))
        conn.commit()
        conn.close()
        print(f"Article ID {article_id} deleted successfully!")
