# PectoTaskCMS

A simple Content Management System (CMS) to manage words and phrases in a local SQLite database using Flask.

## Features

- **View Words and Phrases**: Displays a paginated list of words and phrases with their translation and example sentences (if available).
- **Edit Words and Phrases**: Allows users to edit the word, translation, and example sentence.
- **Save Updates**: Edits are saved back to the local SQLite database.
- **Search and Filter**: Users can search for words by keyword.
- **Load Initial Data**: Initial data is loaded from a provided JSON file and populated into the local database.

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy
- flask-paginate

## Installation

1 - Install the required dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Open the browser and navigate to http://127.0.0.1:5000 to access the CMS.

Usage
The main page lists the words and phrases stored in the SQLite database.
You can search for words using the search bar.
To edit a word, click the "Edit" button next to it, make changes, and click "Update Word".
Updates will be saved to the SQLite database.
