# Scripts for processing corpus of ePub files
This folder contains a collection of scripts that I used to process six of Karl Ove Knausgaard's books in order to assemble a useable corpus. I then used spaCy's NamedEntityRecognizer to extract all of the named entities (people, places, works of art, etc). This data is part of a larger project I am working on that stores the data in a backend (django and postgres) and displays the data in an interactable frontend (node.js, react, typescript)

## File overview

- `argparse_utils.py` -- contains various utility functions for the CLI
- `clean_book_[1-6].py` -- These scripts remove the ebook metadata (mostly html tags) and outputs the raw text into a file
- `export_to_json.py` -- takes a pickled spaCy data file and exports it into a JSON file (to be imported into the db)
- `parsing_tools.py` -- contains a helper function for removing a given regex from a string
- `pickle_books.py` -- allows the user to specify a spaCy model and an input text file and then processes the file and outputs the spaCy data into a compressed pickle file

Most of the files have more details explaining the usage.
