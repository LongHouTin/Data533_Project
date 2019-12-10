import os, sys
# os.chdir("C:/users/longh/desktop/python_working directory")
print(sys.path)

import unittest
class TestHSIhistoric(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        import numpy as np, pandas as pd
        import fed.HSI.instant as it, fed.HSI.historic as ht
        cls.constituents=it.instant().stocks().iloc[:,0].apply(lambda x: x[1:]) # constituents is a pd.Series consisting of the corresponding codes of the current 50 constitudent stocks of the Hang Seng Index on yahoo
        cls.stocks=cls.constituents.sample(np.random.randint(2,51,1),replace=False) # np.random.permutation(constituents)
        cls.num=len(cls.stocks)
        #cls.obs=ht.historic(cls.stocks,startdate="2018-01-01",enddate="2018-12-31") # again, sutteting a pd.Series using np.array of length one does NOT return a scalar type, but a pd.Series of length 1
        #cls.obs=ht.historic(cls.stocks,startdate="2018-01-01")
        #cls.obs=ht.historic(cls.stocks,enddate="2018-12-31")
        #cls.obs=ht.historic(cls.stocks)
        
        cls.dumnum=len("0001.HK")
        cls.dum=ht.historic("0001.HK",startdate="2018-01-01",enddate="2018-12-31") # again, sutteting a pd.Series using np.array of length one does NOT return a scalar type, but a pd.Series of length 1
        cls.dum1=ht.historic("0001.HK",startdate="2018-01-01")
        cls.dum2=ht.historic("0001.HK",enddate="2018-12-31")
        cls.dum3=ht.historic("0001.HK")
        
        cls.num=len(["0001.HK","0005.HK"])
        cls.obs=ht.historic(["0001.HK","0005.HK"],startdate="2018-01-01",enddate="2018-12-31") # again, sutteting a pd.Series using np.array of length one does NOT return a scalar type, but a pd.Series of length 1
        cls.obs1=ht.historic(["0001.HK","0005.HK"],startdate="2018-01-01")
        cls.obs2=ht.historic(["0001.HK","0005.HK"],enddate="2018-12-31")
        cls.obs3=ht.historic(["0001.HK","0005.HK"])
        
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def test_getprices(self):
        import numpy as np, pandas as pd
        
        self.assertIsNotNone(self.__class__.dum.getprices())
        self.assertIsInstance(self.__class__.dum.getprices(),pd.Series)
        self.assertTrue(np.array(self.__class__.dum.getprices().map(type).isin([float])).all()) # pd.nan is of type float64
        self.assertIn(self.__class__.dum.getreturns().index.dtype,["datetime64[ns]","<M8[ns]"])        
        
        print(self.__class__.num) # The dots (.) are unittest's default output when a test passes.
        self.assertIsNotNone(self.__class__.obs.getprices())
        self.assertIsInstance(self.__class__.obs.getprices(),pd.DataFrame)
        self.assertEqual(self.__class__.obs.getprices().shape[1],self.__class__.num) # 247 trading day per year, 2019-11-18 see NaN in China Enterprises
        self.assertTrue(np.array(self.__class__.obs.getprices().applymap(type).isin([float])).all()) # pd.nan is of type float64
        self.assertIn(self.__class__.obs.getreturns().index.dtype,["datetime64[ns]","<M8[ns]"])
    
    def test_getreturns(self):
        import numpy as np, pandas as pd
        
        self.assertIsNotNone(self.__class__.dum.getreturns())
        self.assertIsInstance(self.__class__.dum.getreturns(),pd.Series)
        self.assertTrue(np.array(self.__class__.dum.getreturns().map(type).isin([float])).all())
        self.assertIn(self.__class__.dum.getreturns().index.dtype,["datetime64[ns]","<M8[ns]"])
        
        print(self.__class__.num) # The dots (.) are unittest's default output when a test passes.
        self.assertIsNotNone(self.__class__.obs.getreturns())
        self.assertIsInstance(self.__class__.obs.getreturns(),pd.DataFrame)
        self.assertEqual(self.__class__.obs.getreturns().shape[1],self.__class__.num)
        self.assertTrue(np.array(self.__class__.obs.getreturns().applymap(type).isin([float])).all())
        self.assertIn(self.__class__.obs.getreturns().index.dtype,["datetime64[ns]","<M8[ns]"])
    
    def test_getlogreturns(self):
        self.assertIsNotNone(self.__class__.dum.getlogreturns())
        
        self.assertIsNotNone(self.__class__.obs.getlogreturns())
    
    def test_plotprices(self):
        self.assertIsNone(self.__class__.dum.plotprices())
        
        self.assertIsNone(self.__class__.obs.plotprices())
    
    def test_plotreturns(self):
        self.assertIsNone(self.__class__.dum.plotreturns())    
        self.assertIsNone(self.__class__.dum.plotreturns(log=True))
        
        self.assertIsNone(self.__class__.obs.plotreturns())    
        self.assertIsNone(self.__class__.obs.plotreturns(log=True))
        
        
        
"""        
if __name__=="__main__":
        
    # Call the test without building a test suite
    #unittest.main()
    
    # Build the test suite, and add the test classes that contain different test cases
    HSIsuite2=unittest.TestSuite()
    #HSIsuite.addTest(TestHSI("test_stocks"))
    #HSIsuite.addTest(TestHSI("test_indices"))
    HSIsuite2.addTests([TestHSIhistoric("test_getprices"),TestHSIhistoric("test_getreturns"),TestHSIhistoric("test_getlogreturns"),TestHSIhistoric("test_plotprices"),TestHSIhistoric("test_plotreturns")])
    unittest.TextTestRunner().run(HSIsuite2)
"""        

