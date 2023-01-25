import os
import unittest
from solution_2 import generate_csv


class LambTests(unittest.TestCase):
    def test_generate_csv(self):
        """
        Assert that the generated file has correct number of rows and columns
        """
        number_of_rows = 20
        generate_csv(number_of_rows, "test.csv")
        with open("test.csv") as test_file:
            lines = test_file.readlines()
            self.assertEqual(
                len(lines[0].split(",")), 2, "It generated correct number of columns"
            )
            self.assertEqual(
                len(lines), number_of_rows, "It generated correct number of rows"
            )
        os.remove("test.csv")


if __name__ == "__main__":
    unittest.main()
