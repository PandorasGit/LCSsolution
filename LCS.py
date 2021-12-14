import unittest


class MatrixNode:
    """Node in the matrix used to read the LCS"""

    def __init__(self, direction, length, letter=None):
        self.direction = direction
        self.length = length
        self.letter = letter


class LCS:

    def __init__(self, first_string, second_string):

        def determine_longer_string():
            """Decide which string should be considered the first string regardless of entry"""
            if len(first_string) < len(second_string):
                self.first_string = first_string
                self.second_string = second_string
            else:
                self.first_string = second_string
                self.second_string = first_string

        determine_longer_string()
        self.first_length = len(self.first_string)+1
        self.second_length = len(self.second_string)+1
        null_node = MatrixNode("no where", 0)
        self.solution_matrix = [[null_node for _ in range(self.second_length)] for _ in range(self.first_length)]

    def lcs(self):
        """Calculate the length of an LCS"""

        def lcs_recursive(index_of_first_string, index_of_second_string):
            """Recursive call to loop calculate length"""
            if index_of_first_string == 0 or index_of_second_string == 0:
                return 0

            if self.first_string[index_of_first_string - 1] == self.second_string[index_of_second_string - 1]:

                matrix_node = MatrixNode("up right",
                                         lcs_recursive(index_of_first_string - 1, index_of_second_string - 1) + 1,
                                         self.first_string[index_of_first_string - 1])

                self.solution_matrix[index_of_first_string][index_of_second_string] = matrix_node
                return matrix_node.length

            length_lcs_with_index_of_second_decreased = lcs_recursive(index_of_first_string, index_of_second_string - 1)
            length_lcs_with_index_of_first_decreased = lcs_recursive(index_of_first_string-1, index_of_second_string)

            if length_lcs_with_index_of_first_decreased >= length_lcs_with_index_of_second_decreased:
                matrix_node = MatrixNode("left", length_lcs_with_index_of_first_decreased)
                self.solution_matrix[index_of_first_string][index_of_second_string] = matrix_node
                return matrix_node.length
            else:
                matrix_node = MatrixNode("up", length_lcs_with_index_of_second_decreased)
                self.solution_matrix[index_of_first_string][index_of_second_string] = matrix_node
                return matrix_node.length

        return lcs_recursive(self.first_length-1, self.second_length-1)

    def read_solution(self):
        """Uses Matrix to calculate a LCS, not the only one tho"""
        def reverse_string(string_to_be_reversed):
            """Reverse a string"""
            new_string = ""
            for s in range(len(string_to_be_reversed)):
                new_string += string_to_be_reversed[len(string_to_be_reversed)-s-1]
            return new_string

        index_first = self.first_length-1
        index_second = self.second_length-1
        solution = ""

        while True:
            if index_first == 0 or index_second == 0:
                return reverse_string(solution)
            if self.solution_matrix[index_first][index_second].direction is "up right":
                solution += self.solution_matrix[index_first][index_second].letter
                index_first -= 1
                index_second -= 1
            elif self.solution_matrix[index_first][index_second].direction is "up":
                index_second -= 1
            else:
                index_first -= 1


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

    def test_lcs_of_string_ab_and_ba(self):
        string_x = "ab"
        string_y = "ba"
        lcs = LCS(string_x, string_y)
        lcs.lcs()
        self.assertEqual("b", lcs.read_solution())

    def test_lcs_from_homework(self):
        string_x = "AACGTCGTGA"
        string_y = "TCTTCTGGCTAA"
        lcs = LCS(string_x, string_y)
        lcs.lcs()
        self.assertEqual("CTCGTA", lcs.read_solution())

    def test_alternate_lcs_from_homework(self):
        string_x = "AACGTCGTG"
        string_y = "TCTTCTG"
        lcs = LCS(string_x, string_y)
        lcs.lcs()
        self.assertEqual("CTCTG", lcs.read_solution())


def main():
    unittest.main()


if __name__ == '__main__':
    main()
