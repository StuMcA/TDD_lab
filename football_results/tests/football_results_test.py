import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    def setUp (self):
        final_scores = [
            {"home score":"4", "away score":"0"},
            {"home score":"0", "away score":"4"},
            {"home score":"0", "away score":"0"}
        ]

    # Test we get the right result string for a final score dictionary representing -
    def test_get_result__home_win(self):
        self.assertEqual("home score:4, away score:0", get_result(final_scores[0]))
        # Home win
        # Away win
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 


if __name__ == "__main__":
    unittest.main()
