import unittest

from helper import extension_checker, output_file_creator


class TestExtensionChecker(unittest.TestCase):
    def test_extension_checker_txt(self):
        result = extension_checker("1.txt")
        self.assertTrue(result)

    def test_extension_checker_md(self):
        result = extension_checker("1.md")
        self.assertTrue(result)

    def test_extension_checker_anything(self):
        # result should be the same for any other file extension that is not the supported ones
        result = extension_checker("1.html")
        self.assertFalse(result)


class TestOutputFileCreatorFileName(unittest.TestCase):
    def test_creating_a_file(self):
        created_file_name = output_file_creator("test.txt", "test")
        self.assertEqual(created_file_name, r"test\test.html")

    def test_unable_to_create_file(self):
        self.assertRaises(Exception, output_file_creator, 1, "test")
        self.assertRaises(Exception, output_file_creator, "test.md", 1)


if __name__ == "__main__":
    unittest.main()
