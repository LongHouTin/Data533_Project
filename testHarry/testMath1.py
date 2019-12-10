#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from fed.calculate.fmath import netPurchaseChange
from fed.calculate.fmath import netPurchase

class TestFmath1(unittest.TestCase):
    
    def setUp(self):
        print("this is setUp")
        
    def tearDown(self):
        print("this is tearDown")
    
    
    
    def test_netPurchaseChange(self):
        self.assertEqual(netPurchaseChange("2019-11-22"),0.0826)
        self.assertEqual(netPurchaseChange("2019-11-25"),-0.1501)
        self.assertEqual(netPurchaseChange("2019-11-26"),0.062)
        self.assertEqual(netPurchaseChange("2019-11-27"),0.2158)
        self.assertEqual(netPurchaseChange("2019-10-31"),0.2119)
        self.assertEqual(netPurchaseChange("2019-10-28"),-0.0098)
    
    def test_netPurchase(self):
        self.assertEqual(netPurchase("2019-11-22"),80.225)
        self.assertEqual(netPurchase("2019-11-25"),68.5)
        self.assertEqual(netPurchase("2019-11-26"),70.545)
        self.assertEqual(netPurchase("2019-11-27"),87.7)
        self.assertEqual(netPurchase("2019-10-31"),69.682)
        self.assertEqual(netPurchase("2019-10-28"),76.547)

