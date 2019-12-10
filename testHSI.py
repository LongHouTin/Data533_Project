import unittest
from fed.crawl.crawl import webcrawl
import fed.HSI.instant as it, fed.HSI.historic as ht
import testSam.testHSIinstant, testSam.testHSIhistoric
# importing pandas and numpy throws errors, why ???

HSIsuite=unittest.TestSuite()
HSIsuite.addTests([testSam.testHSIinstant.TestHSIinstant("test_indices"),testSam.testHSIinstant.TestHSIinstant("test_stocks")])
HSIsuite.addTests([testSam.testHSIhistoric.TestHSIhistoric("test_getprices"),testSam.testHSIhistoric.TestHSIhistoric("test_getreturns"),testSam.testHSIhistoric.TestHSIhistoric("test_getlogreturns"),testSam.testHSIhistoric.TestHSIhistoric("test_plotprices"),testSam.testHSIhistoric.TestHSIhistoric("test_plotreturns")])
