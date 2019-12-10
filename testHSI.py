"""
import numpy as np, pandas as pd
import fed.HSI.instant as it, fed.HSI.historic as ht
    
import unittest
import testSam.testHSIinstant, testSam.testHSIhistoric


HSIsuite=unittest.TestSuite()
HSIsuite.addTests([testSam.testHSIinstant.TestHSIinstant("test_indices"),testSam.testHSIinstant.TestHSIinstant("test_stocks")])
HSIsuite.addTests([testSam.testHSIhistoric.TestHSIhistoric("test_getprices"),testSam.testHSIhistoric.TestHSIhistoric("test_getreturns"),testSam.testHSIhistoric.TestHSIhistoric("test_getlogreturns"),testSam.testHSIhistoric.TestHSIhistoric("test_plotprices"),testSam.testHSIhistoric.TestHSIhistoric("test_plotreturns")])
unittest.TextTestRunner().run(HSIsuite)
"""

pass