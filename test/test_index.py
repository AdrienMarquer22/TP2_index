import unittest 
from index.index import Index

class TestIndex(unittest.TestCase):
    def setUp(self):
        self.index = Index()

    def test_load_json(self):
        self.index.load_json()
        self.assertIsInstance(self.index.liste_urls, list)

    def test_get_title_list(self):
        self.index.liste_urls = ["https://www.example.com"]
        self.index.get_title_list()
        self.assertEqual(self.index.title_list, ['Example Domain'])

    def test_tokenisation(self):
        self.index.liste_urls = ["https://www.example.com","https://www.example.com"]
        self.index.get_title_list()
        self.index.tokenisation()
        self.assertEqual(self.index.title_tokenize[0], ['example','domain'])
        self.assertEqual(self.index.title_tokenize_flatten, ['example','domain','example','domain'])

    def test_create_index_no_po(self):
        self.index.liste_urls = ["https://www.example.com","https://www.example.com"]
        self.index.create_index_no_pos()
        self.assertIsInstance(self.index.index_no_pos, dict)
        self.assertEqual(self.index.index_no_pos["example"],2)


    def test_create_index_pos(self):
        self.index.liste_urls = ["https://www.example.com","https://www.example.com"]
        self.index.create_index_pos()
        self.assertIsInstance(self.index.index_pos, dict)
        self.assertIsInstance(self.index.index_pos["example"], dict)
        self.assertIsInstance(self.index.index_pos["example"][1], list)
        self.assertEqual(self.index.index_pos["example"][1],[0])
        self.assertEqual(self.index.index_pos["domain"][0],[1])

    def test_create_stemmer_no_pos(self):
        self.index.title_tokenize.append(['circuit','circuits'])
        self.index.liste_urls = ["https://www.example.com","https://www.example.com"]
        self.index.create_stemmer_index_no_pos()
        self.assertIsInstance(self.index.stemmer_index_no_pos, dict)
        self.assertEqual(self.index.stemmer_index_no_pos["circuit"],2)

    def test_statistique(self):
        self.index.liste_urls = ["https://www.example.com","https://www.example.com"]
        self.index.get_title_list()
        self.index.tokenisation()
        self.index.statistique()
        self.assertIsInstance(self.index.dict_statistique, dict)
        self.assertEqual(self.index.dict_statistique["Number of document"],2)
        self.assertEqual(self.index.dict_statistique["Number of total tokens"],4)
        self.assertEqual(self.index.dict_statistique["Number of unique tokens"],2)
        self.assertEqual(self.index.dict_statistique["Average of token pre document"],2)
        self.assertEqual(self.index.dict_statistique["Variance of the number of token"],0)