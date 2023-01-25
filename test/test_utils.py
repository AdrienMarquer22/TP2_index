import unittest
import requests
from bs4 import BeautifulSoup
import re
import socket
from index.utils import *

class TestLoadPage(unittest.TestCase):
    def test_load_page_success(self):
        # Test a successful page load
        url = 'https://www.example.com'
        result = load_page(url)
        self.assertIsInstance(result, BeautifulSoup)

    def test_load_page_failure(self):
        # Test a failed page load
        url = 'https://www.example.com/404'
        result = load_page(url)
        self.assertFalse(result)

class TestTokenize(unittest.TestCase):
    def test_tokenize(self):
        # Test tokenizing a string
        string = "This is a test string."
        result = tokenize(string)
        self.assertEqual(result, ['This', 'is', 'a', 'test', 'string.'])

class TestCleanText(unittest.TestCase):
    def test_clean_text(self):
        # Test cleaning a string
        string = "This is a test string! 123"
        result = clean_text(string)
        self.assertEqual(result, 'this is a test string 123')

class TestFlattenList(unittest.TestCase):
    def test_flatten_list(self):
        # Test flattening a list of lists
        lists = [[1, 2, 3], [4, 5], [6]]
        result = flatten_list(lists)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])
