import os, sys
# os.chdir("C:/users/longh/desktop/python_working directory")
print(sys.path)


import unittest
"""
The main differenc of setUp() and setUpClass is that 
setUpClass is called only once and that is before all 
the tests, while setUp is called immediately before 
each and every test.

SetUp() is called before every test method, whereas 
setUpClass() is called once before all tests. 
Any expensive operations that many of your tests can 
take advantage of, should go in setUpClass()

From within setUp(), you can directly access variable 
within setUpClass without the 'cls' notation. Or 
sccessed by self.__class__.variableName.

By adding the @classmethod decorator, you are saying 
that when TestHSI.setupClass() is called, the first 
argument is the class TestHSI itself.
"""
class TestHSIinstant(unittest.TestCase):
    
    # Run once for the whole test class
    @classmethod
    def setUpClass(cls):
        import numpy as np, pandas as pd
        import fed.HSI.instant as it        
        cls.dices=it.instant().indices() # stay coll, N/A pop up since the market is not open, nothing's wrong with the module
        cls.ocks=it.instant().stocks()
        print("setUpClass")
    
    # Run before every test    
    def setUp(self):
        #print("setUp")
        pass
        
    def tearDown(self):
        #print("TearDown")
        pass
    
    @classmethod
    def tearDownClass(cls):
        #print("TearDownClass")
        pass
    
    # Test 1     
    def test_indices(self):
        import numpy as np, pandas as pd
        import random
        self.assertIsNotNone(self.__class__.dices)
        self.assertIsInstance(self.__class__.dices,pd.DataFrame)
        self.assertEqual(self.__class__.dices.shape,(5,3)) 
        # self.assertTrue(pd.Series(self.__class__.dices.iloc[:,i].dtype for i in range(3)).isin(["object"]).all()) # inconssitent results in spyder3 and jupyter notebook
        self.assertIsNotNone(self.__class__.dices.iloc[np.random.randint(0,3,1),random.sample([0,2],1)].applymap(lambda x: float(x.replace(",","")))) # applymap is for pd.DF 
        # random.choices([1,2],k=3) is sample with replacement
        # random.sample([1,2],k=2) is sample without replacement, k must be samller than or equal to the length of the list 
        # focus on only column 0 or 2 is because when the market is not open the middle column "Open" will be a bs4.element.NavigableString "N/A"
        self.assertFalse(self.__class__.dices.iloc[int(np.random.randint(0,3,1)),[0,2]].apply(lambda x: float(x.replace(",",""))).isnull().any()) # apply is for pd.S
        # subsetting DF with a array of length 1 does NOT returns pd.Series, but a DataFrame of shape(1,n)
    
    # Test 2    
    def test_stocks(self):
        import numpy as np, pandas as pd
        self.assertIsNotNone(self.__class__.ocks)
        self.assertIsInstance(self.__class__.ocks,pd.DataFrame)
        self.assertEqual(self.__class__.ocks.shape,(50,8)) 
        # self.assertTrue(pd.Series(self.__class__.ocks.iloc[:,i].dtype for i in range(8)).isin(["object"]).all()) # inconssitent results in spyder3 and jupyter notebook
        self.assertEqual(self.__class__.ocks.iloc[:,0].isin(["00001.HK"]).sum(),1)
        self.assertTrue("00001.HK" in list(self.__class__.ocks.iloc[:,0])) # essentially same as the previous assertion statement




"""
if __name__=="__main__":
        
    # Call the test without building a test suite
    #unittest.main(argv=[''],verbosity=2,exit=False)

    # Build the test suite, and add the test classes that contain different test cases
    HSIsuite1=unittest.TestSuite()
    #HSIsuite.addTest(TestHSI("test_stocks"))
    #HSIsuite.addTest(TestHSI("test_indices"))
    HSIsuite1.addTests([TestHSIinstant("test_indices"),TestHSIinstant("test_stocks")])
    unittest.TextTestRunner().run(HSIsuite1)
"""    