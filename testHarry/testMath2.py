#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from fed.calculate.fmath import nasdaq
from fed.calculate.fmath import vix

class TestFmath2(unittest.TestCase):
    def setUp(self):
        print("this is setUp")
        
    def tearDown(self):
        print("this is tearDown")
    
    
    
    def test_nasdaq(self):
        self.assertEqual(nasdaq("2019-11-27"),8705.17)
        self.assertEqual(nasdaq("2019-11-15"),8540.82)
        self.assertEqual(nasdaq("2019-11-06"),8410.62)
        self.assertEqual(nasdaq("2019-11-25"),8632.48)
        self.assertEqual(nasdaq("2019-11-08"),8475.31)
        
    def test_vix(self):
        self.assertEqual(vix("2019-11-27"),11.75)
        self.assertEqual(vix("2019-11-11"),12.69)
        self.assertEqual(vix("2019-11-26"),11.54)
        self.assertEqual(vix("2019-11-29"),12.62)
        self.assertEqual(vix("2019-12-02"),14.91)

