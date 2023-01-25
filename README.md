# Adrien MARQUER - TP2 Crawler


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

## Usage

Launch with the command 
```bash
python3 main.py [--type type][--npythonopos][--pos][--stem_nopos][--name name]
```

There is 6 arguments to use :

- `--type` : The html tag thaou want to use (`default=title`)
- `--nopos` : If you want non positionnal index (`default=False`)
- `--pos` : If you want positionnal index (`defaul="False"`)
- `--stem_nopos` : If you want non positionnal index with stemmer (`defaul="False"`)
- `--name` : name for the file to save




```bash
# Launch the tests 
python3 -m unittest discover test/
#
python3 main.py --type title --nopos --name title.non_pos_index
#
python3 main.py --type title --pos --name title.pos_index
#
python3 main.py --type title --stem_nopos --name mon_stemmer.title.non_pos_index
# with h1 cintent
python3 main.py --type h1 --stem_nopos --name mon_stemmer.h1.non_pos_index

```


## Class

### Index

The `Index` class is a powerful tool for creating and manipulating indexes of text data. It allows you to load a JSON file containing a list of URLs, extract the title or other specified element of each page, tokenize the text, and create various types of indexes for the tokens. The class also provides methods for computing statistics about the index and for saving the index to a file.
Usage

Here is an example of how to use the Index class:
```Python
# Create an instance of the class
index = Index()

# Load a JSON file containing a list of URLs
index.load_json("data/crawled_urls.json")

# Extract the title of each page and store it in a list
index.get_title_list()

# Tokenize the titles and flatten the list of lists
index.tokenisation()

# Create a dictionary-based index (no positional information)
index.create_index_no_pos()

# Create a dictionary-based index (with positional information)
index.create_index_pos()

# Create a stemmer index (no positional information)
index.create_stemmer_index_no_pos()

# Compute statistics about the index
index.statistique()

# Save the index to a file
index.save_index_no_pos("title.non_pos_index.json")
index.save_index_pos("title.pos_index.json")
index.save_stemmer_index_no_pos("mon_stemmer.title.non_pos_index.json")
# Save the statistique
index.save_statistique()
```

#### Parameters

The `Index` class takes one optional parameter:

+ `type`: Specifies the type of element to extract from each page (default is 'title').

#### Methods

The `Index` class provides the following methods:

+ `load_json(path)`: loads a JSON file containing a list of URLs.
+ `get_title_list()`: Extracts the title of each page and store it in a list.
+ `tokenisation()`: Tokenize the titles and flatten the list of lists.
+ `create_index_no_pos()`: Create a dictionary-based index (no positional information).
+ `create_index_pos()`: Create a dictionary-based index (with positional information).
+ `create_stemmer_index_no_pos()`: Create a stemmer index