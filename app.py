from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine


def create_author():
    name = input("Enter author's name: ")
    if len(name.strip()) == 0:
        print("Error: Name cannot be empty.")
        return

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
    conn.commit()
    print(f"Author '{name}' created successfully!")
    conn.close()


def create_magazine():
    name = input("Enter magazine name: ")
    category = input("Enter magazine category: ")

    if len(name) < 2 or len(name) > 16:
        print("Error: Name must be between 2 and 16 characters.")
        return
    if len(category.strip()) == 0:
        print("Error: Category cannot be empty.")
        return

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (name, category))
    conn.commit()
    print(f"Magazine '{name}' created successfully!")
    conn.close()


def create_article():
    title = input("Enter article title: ")
    content = input("Enter article content: ")
    author_id = input("Enter author ID: ")
    magazine_id = input("Enter magazine ID: ")

    if len(title) < 5 or len(title) > 50:
        print("Error: Title must be between 5 and 50 characters.")
        return
    if len(content.strip()) == 0:
        print("Error: Content cannot be empty.")
        return

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            'INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
            (title, content, author_id, magazine_id),
        )
        conn.commit()
        print(f"Article '{title}' created successfully!")
    except Exception as e:
        print(f"Error creating article: {e}")
    finally:
        conn.close()


def view_authors():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM authors')
    authors = cursor.fetchall()
    if authors:
        print("\nAuthors:")
        for author in authors:
            print(f"ID: {author['id']}, Name: {author['name']}")
    else:
        print("No authors found.")
    conn.close()


def view_magazines():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM magazines')
    magazines = cursor.fetchall()
    if magazines:
        print("\nMagazines:")
        for magazine in magazines:
            print(f"ID: {magazine['id']}, Name: {magazine['name']}, Category: {magazine['category']}")
    else:
        print("No magazines found.")
    conn.close()


def view_articles():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()
    if articles:
        print("\nArticles:")
        for article in articles:
            print(f"ID: {article['id']}, Title: {article['title']}, Author ID: {article['author_id']}, Magazine ID: {article['magazine_id']}")
    else:
        print("No articles found.")
    conn.close()


def update_article_content():
    article_id = input("Enter the article ID to update: ")
    new_content = input("Enter the new content for the article: ")

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            'UPDATE articles SET content = ? WHERE id = ?', (new_content, article_id)
        )
        conn.commit()
        print(f"Article ID {article_id} updated successfully!")
    except Exception as e:
        print(f"Error updating article: {e}")
    finally:
        conn.close()


def delete_article():
    article_id = input("Enter the article ID to delete: ")

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM articles WHERE id = ?', (article_id,))
        conn.commit()
        print(f"Article ID {article_id} deleted successfully!")
    except Exception as e:
        print(f"Error deleting article: {e}")
    finally:
        conn.close()


def list_articles_by_author():
    author_id = input("Enter author ID: ")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        SELECT articles.title, magazines.name 
        FROM articles
        JOIN magazines ON articles.magazine_id = magazines.id
        WHERE articles.author_id = ?
        ''',
        (author_id,),
    )
    articles = cursor.fetchall()
    if articles:
        print(f"\nArticles by Author ID {author_id}:")
        for article in articles:
            print(f"Title: {article['title']}, Magazine: {article['name']}")
    else:
        print(f"No articles found for Author ID {author_id}.")
    conn.close()


def main():
    create_tables()  # Ensure tables are initialized
    while True:
        print("\n--- Menu ---")
        print("1. Create Author")
        print("2. Create Magazine")
        print("3. Create Article")
        print("4. View All Authors")
        print("5. View All Magazines")
        print("6. View All Articles")
        print("7. Update Article Content")
        print("8. Delete Article")
        print("9. List Articles by Author")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_author()
        elif choice == "2":
            create_magazine()
        elif choice == "3":
            create_article()
        elif choice == "4":
            view_authors()
        elif choice == "5":
            view_magazines()
        elif choice == "6":
            view_articles()
        elif choice == "7":
            update_article_content()
        elif choice == "8":
            delete_article()
        elif choice == "9":
            list_articles_by_author()
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
