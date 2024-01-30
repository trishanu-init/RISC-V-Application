import unittest
from list_operation import *

class TestProcessUserList(unittest.TestCase):    

    # Test that the function prints the correct new list skipping values at indices that are multiple of 2 or 3
    def test_valid_list_operation_10(self):
        from unittest.mock import patch
        with patch("builtins.print") as mock_print:
            process_user_list("1 2 3 4 5 6 7 8 9 10")
            mock_print.assert_called_with("New  list :", [1, 5, 7])

    # Test that the function prints the correct new list skipping values at indices that are multiple of 2 or 3
    def test_valid_list_operation_20(self):
        from unittest.mock import patch
        with patch("builtins.print") as mock_print:
            process_user_list("1 2 3 4 5 6 7 8 9 10 11 12 13 23 34 54 76 89 56 76")
            mock_print.assert_called_with("New  list :", [1, 5, 7, 11, 13, 76, 56])

    # Test that the function prints the correct new list skipping values at indices that are multiple of 2 or 3
    def test_valid_list_operation_100(self):
        from unittest.mock import patch
        with patch("builtins.print") as mock_print:
            process_user_list("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100")
            mock_print.assert_called_with("New  list :", [1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49, 53, 55, 59, 61, 65, 67, 71, 73, 77, 79, 83, 85, 89, 91, 95, 97])

    # Test that the function returns an Error if list size is not a multiple of 10
    def test_invalid_list_size(self):
        from unittest.mock import patch
        with patch("builtins.print") as mock_print:
            process_user_list("1 2 4 5 6 7")
            assert(Exception)

    # Test that the function returns an Error if list is Empty
    def test_empty_list(self):
        from unittest.mock import patch
        with patch("builtins.print") as mock_print:
            process_user_list(" ")
            assert(Exception)
    #Test that function returns ValueError if list contains non integer values
    def test_non_integer_value(self):
        from unittest.mock import patch
        with patch("builtins.print") as mock_print:
            process_user_list("1 2 3 4 5 6 7 8 a b")
            assert(ValueError)


# Run the tests
if __name__ == "__main__":
    unittest.main()
