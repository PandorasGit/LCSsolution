import unittest


class LCS:

    def __init__(self, first_string, second_string):
        self.first_string = first_string
        self.second_string = second_string

    def lcs(self):
        """Calculate the length of an LCS"""
        def lcs_recursive(index_of_first_string, index_of_second_string):
            """Recursive call to loop calculate length"""
            if index_of_first_string == 0 or index_of_second_string == 0:
                return 0
            if self.first_string[index_of_first_string-1] == self.second_string[index_of_second_string-1]:
                return lcs_recursive(index_of_first_string-1, index_of_second_string-1) + 1
            return max(
                lcs_recursive(index_of_first_string, index_of_second_string-1),
                lcs_recursive(index_of_first_string-1, index_of_second_string)
            )
        return lcs_recursive(len(self.first_string), len(self.second_string))


class TestClass(unittest.TestCase):
    """
    Class for testing LCS Strings
    """
    def test_lcs_length_of_empty_strings(self):
        string_x = ""
        string_y = ""
        lcs = LCS(string_x, string_y)
        self.assertEqual(0, lcs.lcs())

    def test_lcs_length_of_same_size_strings(self):
        string_x = "GamInG"
        string_y = "Gaming"
        lcs = LCS(string_x, string_y)
        self.assertEqual(4, lcs.lcs())

    def test_lcs_length_from_homework(self):
        string_x = "AACGTCGTGA"
        string_y = "TCTTCTGGCTAA"
        lcs = LCS(string_x, string_y)
        self.assertEqual(6, lcs.lcs())

    def test_lcs_length_from_random_string(self):
        string_x = "xjdkhfgbns"
        string_y = "slizudjfg"
        lcs = LCS(string_x, string_y)
        self.assertEqual(3, lcs.lcs())


def main():
    unittest.main()


if __name__ == '__main__':
    main()
