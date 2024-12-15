import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine
from database.connection import get_db_connection
from database.setup import create_tables


class TestModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Initialize the database before tests."""
        create_tables()

    def setUp(self):
        """Clear the database tables before each test."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM authors")
        cursor.execute("DELETE FROM articles")
        cursor.execute("DELETE FROM magazines")
        conn.commit()
        conn.close()

    def test_author_creation(self):
        """Test creating an author."""
        author_id = Author.create("John Doe")
        self.assertIsNotNone(author_id)

        # Verify in database
        authors = Author.get_all()
        self.assertEqual(len(authors), 1)
        self.assertEqual(authors[0]['name'], "John Doe")

    def test_magazine_creation(self):
        """Test creating a magazine."""
        magazine_id = Magazine.create("Tech Weekly", "Technology")
        self.assertIsNotNone(magazine_id)

        # Verify in database
        magazines = Magazine.get_all()
        self.assertEqual(len(magazines), 1)
        self.assertEqual(magazines[0]['name'], "Tech Weekly")
        self.assertEqual(magazines[0]['category'], "Technology")

    def test_article_creation(self):
        """Test creating an article."""
        author_id = Author.create("John Doe")
        magazine_id = Magazine.create("Tech Weekly", "Technology")
        article_id = Article.create("Test Title", "Test Content", author_id, magazine_id)
        self.assertIsNotNone(article_id)

        # Verify in database
        articles = Article.get_all()
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0]['title'], "Test Title")
        self.assertEqual(articles[0]['author_id'], author_id)
        self.assertEqual(articles[0]['magazine_id'], magazine_id)

    def test_article_update_content(self):
        """Test updating article content."""
        author_id = Author.create("Jane Smith")
        magazine_id = Magazine.create("Health Monthly", "Health")
        article_id = Article.create("Old Title", "Old Content", author_id, magazine_id)

        # Update content
        success = Article.update_content(article_id, "Updated Content")
        self.assertTrue(success)

        # Verify in database
        articles = Article.get_all()
        self.assertEqual(articles[0]['content'], "Updated Content")

    def test_article_deletion(self):
        """Test deleting an article."""
        author_id = Author.create("Jane Smith")
        magazine_id = Magazine.create("Science Today", "Science")
        article_id = Article.create("Delete Me", "Some Content", author_id, magazine_id)

        # Delete article
        success = Article.delete(article_id)
        self.assertTrue(success)

        # Verify in database
        articles = Article.get_all()
        self.assertEqual(len(articles), 0)

    def test_list_articles_by_author(self):
        """Test listing articles by a specific author."""
        author_id = Author.create("Alice Doe")
        magazine_id = Magazine.create("Fashion Weekly", "Fashion")
        Article.create("Trendy Styles", "Latest trends in fashion.", author_id, magazine_id)
        Article.create("Winter Wear", "Best winter clothing.", author_id, magazine_id)

        # Fetch articles
        articles = Article.get_by_author(author_id)
        self.assertEqual(len(articles), 2)
        self.assertEqual(articles[0]['title'], "Trendy Styles")
        self.assertEqual(articles[1]['title'], "Winter Wear")

    @classmethod
    def tearDownClass(cls):
        """Clean up the database after tests."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS authors")
        cursor.execute("DROP TABLE IF EXISTS articles")
        cursor.execute("DROP TABLE IF EXISTS magazines")
        conn.commit()
        conn.close()


if __name__ == "__main__":
    unittest.main()
