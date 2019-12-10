import unittest
from fed.crawl.crawl import webcrawl
class TestCrawl(unittest.TestCase):
    
    def setUp(self):
        print("this is setUp")
        
    def tearDown(self):
        print("this is tearDown")
    
    def test_webcrawl(self):
        self.assertEqual(webcrawl(),None)  # test should be carried out with internet connection otherwise failed