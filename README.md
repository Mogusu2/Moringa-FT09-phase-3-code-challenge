Here's an updated and appealing README for your project, incorporating the new features and functionalities added to the `app.py` file:

---

# Moringa FT09 Phase 3 Code Challenge: Articles with Database

## Description
This project focuses on implementing a system to manage **Articles**, **Authors**, and **Magazines** with a relational database using **SQLite** and **Python**. The application allows you to create and manage articles, authors, and magazines with clear relationships between them. Additionally, we’ve built a menu-driven interface for CRUD operations, enabling users to perform various actions easily.

## Features
1. **Database Setup**: The database includes three tables:
   - **Authors**: Stores information about authors.
   - **Magazines**: Stores magazine details like name and category.
   - **Articles**: Articles are associated with both authors and magazines, forming key relationships.

2. **CRUD Operations**:
   - **Create**: Allows users to add authors, magazines, and articles to the database.
   - **Read**: View all authors, magazines, and articles stored in the database.
   - **Update**: Users can update the content of articles.
   - **Delete**: Articles can be deleted by their ID.
   - **List Articles by Author**: Retrieve articles written by a specific author along with the associated magazine.

3. **Interactive Menu**: The app runs a menu interface that offers users various choices for interacting with the database.

## File Structure

```
/Moringa-FT09-phase-3-code-challenge
├── /database
│   ├── connection.py       # Database connection string and methods
│   └── setup.py            # SQL queries to create tables and setup the database
├── /models
│   ├── article.py          # Article model with CRUD operations
│   ├── author.py           # Author model with CRUD operations
│   └── magazine.py         # Magazine model with CRUD operations
├── /tests                  # Unit tests for various features
├── app.py                  # Main app file with CRUD operations and menu-driven interface
└── README.md               # Project documentation
```

## Installation

### Requirements
- Python 3.x
- SQLite (comes pre-installed with Python)

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Mogusu2/Moringa-FT09-phase-3-code-challenge.git
   cd Moringa-FT09-phase-3-code-challenge
   ```

2. Install any necessary dependencies (if any are added in the future):
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

## Usage

Once the app is running, you'll be prompted with the following menu options:

### Menu Options:
1. **Create Author**: Add a new author to the system.
2. **Create Magazine**: Add a new magazine along with its category.
3. **Create Article**: Add an article and link it to an author and a magazine.
4. **View All Authors**: Display all authors in the database.
5. **View All Magazines**: Display all magazines in the database.
6. **View All Articles**: Display all articles in the database.
7. **Update Article Content**: Update the content of an existing article.
8. **Delete Article**: Delete an article by its ID.
9. **List Articles by Author**: Retrieve and list articles written by a specific author.
10. **Exit**: Exit the application.

## Example Workflow

1. **Create an Author**: 
   Enter the name of the author when prompted. The system will store this in the `authors` table.

2. **Create a Magazine**: 
   Provide a name and category for the magazine. The system will save this information in the `magazines` table.

3. **Create an Article**: 
   Enter the title, content, author ID, and magazine ID to create an article linked to the chosen author and magazine.

4. **View Data**: 
   You can view a list of all authors, magazines, and articles stored in the database, complete with details like the article's title, associated author, and magazine.

5. **Update and Delete**: 
   You can update article content or delete articles based on their IDs. The system also allows you to list articles written by a specific author.

## Testing

Unit tests are provided in the `/tests` folder to verify the correctness of the CRUD operations and database interactions. These tests ensure that the system functions as expected, including handling edge cases and input validation.

To run the tests, you can use a testing framework like `unittest`:
```bash
python -m unittest discover
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Improvements:
- The README now outlines the main features and functionalities in a structured manner.
- The new CRUD operations and menu system have been clearly described to show what the application offers.
- Installation and usage steps have been included to make it easier for others to get started with the project.

This updated README should make your project more appealing to users and contributors.