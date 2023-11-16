import os
import tempfile
import unittest

from helper import extension_checker, output_file_creator, generate_sidebar



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


class TestGenerateSidebar(unittest.TestCase):
    def setUp(self):
        self.table_of_contents = [
            {
                "label": "TIL How to Get Command Line Arguments in Python",
                "url": "TIL How to Get Command Line Arguments in Python.html",
            },
            {
                "label": "TIL rmtree and os Library",
                "url": "TIL rmtree and os Library.html",
            },
        ]

        self.sidebar_file = "sidebar.py"

        self.invalid_file = "invalid.md"

    def test_generate_sidebar(self):
        result = generate_sidebar(self.sidebar_file)

        expected = (
            "\t\tTable of Contents\n\t\t"
            "<nav>\n\t\t\t"
            "<ul>\n\t\t\t\t<li>"
            '<a href="TIL How to Get Command Line Arguments in Python.html">TIL How to Get Command Line Arguments in Python</a>'
            "</li>\n\t\t\t\t"
            '<li><a href="TIL rmtree and os Library.html">TIL rmtree and os Library</a>'
            "</li>\n\t\t\t</ul>\n\t\t</nav>"
        )

        self.assertEqual(result, expected)

    def test_generate_sidebar_error(self):
        with self.assertRaises(SystemExit):
            generate_sidebar(self.invalid_file)


if __name__ == "__main__":
    unittest.main()
