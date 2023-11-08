import unittest

from file_processors import parse_md


class TestMarkdown(unittest.TestCase):
    def test_convert_bold(self):
        converted_string = parse_md("**Hello World**")
        self.assertEqual(converted_string, "<strong>Hello World</strong>")

    def test_convert_hr(self):
        converted_string = parse_md("---")
        self.assertEqual(converted_string, "<hr>")

    def test_convert_link(self):
        converted_string = parse_md("[YouTube](https://www.youtube.com/)")
        self.assertEqual(
            converted_string, "<a href=https://www.youtube.com/>YouTube</a>"
        )

    # Tests conversion result for both 1 and 3 backticks
    def test_convert_code(self):
        converted_string = parse_md("```Hello world```")
        self.assertEqual(converted_string, "<code>Hello world</code>")

        converted_string = parse_md("`Hello world`")
        self.assertEqual(converted_string, "<code>Hello world</code>")


if __name__ == "__main__":
    unittest.main()
