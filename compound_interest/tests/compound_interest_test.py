import unittest

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):

    # Tests
    def test_100_10_20(self):
        compound_interest = CompoundInterest(100, 10, 20)
        self.assertEqual(732.81, compound_interest.compound_interest_calc())
    # Should return 732.81 given 100 principal, 10 percent, 20 years
    def test_100_6_10(self):
        compound_interest = CompoundInterest(100, 6, 10)
        self.assertEqual(181.94, compound_interest.compound_interest_calc())
    # Should return 181.94 given 100 principal, 6 percent, 10 years
    def test_100000_5_8(self):
        compound_interest = CompoundInterest(100000, 5, 8)
        self.assertEqual(149058.55, compound_interest.compound_interest_calc())
    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
    def test_0_10_19(self):
        compound_interest = CompoundInterest(0, 10, 1)
        self.assertEqual(0.00, compound_interest.compound_interest_calc())
    # Should return 0.00 given 0 principal, 10 percent, 1 year
    def test_100_0_10(self):
        compound_interest = CompoundInterest(100, 0, 10)
        self.assertEqual(100.00, compound_interest.compound_interest_calc())
    # Should return 100.00 given 100 principal, 0 percent, 10 years


    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month
    def test_100_5_8_1000(self):
        monthly_interest = CompoundInterest(100, 5, 8, 1000)
        self.assertEqual(118380.16, monthly_interest.monthly_contribution_calc())
    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month
    def test_100_5_10_1000(self):
        monthly_interest = CompoundInterest(100, 5, 10, 1000)
        self.assertEqual(156093.99, monthly_interest.monthly_contribution_calc())
    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month
    def test_7_8_2006(self):
        monthly_interest = CompoundInterest(116028.86, 7.5, 8, 2006)
        self.assertEqual(475442.59, monthly_interest.monthly_contribution_calc())
    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month
    def test_116028_9_12_1456(self):
        monthly_interest = CompoundInterest(116028.86, 9, 12, 1456)
        self.assertEqual(718335.97, monthly_interest.monthly_contribution_calc())
