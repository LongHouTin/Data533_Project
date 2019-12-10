#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from fed.draw.visualize import linechart,barchart30days,barchartyrs
class TestVisualize(unittest.TestCase):
    
    
    def setUp(self):
        print("this is setUp")
        
    def tearDown(self):
        print("this is tearDown")
        
    def test_linechart(self):
        self.assertEqual(linechart(),None)
        
        
    def test_barchart30days(self):
        self.assertEqual(barchart30days(),None)

        
    def test_barchartyrs(self):
        self.assertEqual(barchartyrs(),None)

