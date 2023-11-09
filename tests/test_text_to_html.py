import os
import tempfile
import unittest

from file_processors import text_to_html


class TestTextToHtmlTxtConversion(unittest.TestCase):
    def setUp(self):
        # Creating a temporary input file with some text content
        self.input_file = tempfile.NamedTemporaryFile(
            mode="w", suffix=".txt", delete=False
        )
        self.input_file.write("This is a test file.\n")
        self.input_file.close()

        # Creating a temporary output directory
        self.output_dir = tempfile.TemporaryDirectory()

        # Defining the stylesheet, language, and sidebar
        self.stylesheet = "https://cdn.jsdelivr.net/npm/water.css@2/out/water.css"
        self.lang = "en-CA"
        self.sidebar = None

    def tearDown(self):
        # Deleting the temporary input file and output directory
        os.remove(self.input_file.name)
        self.output_dir.cleanup()

    def test_text_to_html_txt_conversion(self):
        with self.assertRaises(SystemExit) as cm:
            # Calling the text_to_html function and store the HTML content
            html_content = text_to_html(
                self.input_file.name,
                self.stylesheet,
                self.output_dir.name,
                self.lang,
                self.sidebar,
            )

            self.assertEqual(cm.exception.code, 0)

            # Defining the expected HTML content
            expected_html_content = (
                f"<!DOCTYPE html>\n"
                f'<html lang="{self.lang}">\n'
                f"\t<head>\n"
                f"\t\t<meta charset='utf-8'>\n"
                f"\t\t<title>This is a test file</title>\n"
                f"\t\t<meta name='viewport' content='width=device-width, initial-scale=1'>\n"
                f'\t\t<link rel="stylesheet" type="text/css" href="{self.stylesheet}">\n'
                f"\t</head>\n"
                f"\t<body>\n"
                f"\t\t<p> This is a test file.</p>\n"
                f"\t</body>\n"
                f"</html>"
            )

            # Check if the HTML content matches the expected HTML content
            self.assertEqual(html_content, expected_html_content)

    class TestTextToHtmlMdConversion(unittest.TestCase):
        def tearDown(self):
            os.remove(self.input_file.name)
            self.output_dir.cleanup()

        def test_text_to_html_md_conversion(self):
            with self.assertRaises(SystemExit) as cm:
                html_content = text_to_html(
                    self.input_file.name,
                    self.stylesheet,
                    self.output_dir.name,
                    self.lang,
                    self.sidebar,
                )

                self.assertEqual(cm.exception.code, 0)

                expected_html_content = (
                    f"<!DOCTYPE html>\n"
                    f'<html lang="{self.lang}">\n'
                    f"\t<head>\n"
                    f"\t\t<meta charset='utf-8'>\n"
                    f"\t\t<title>This is a test file</title>\n"
                    f"\t\t<meta name='viewport' content='width=device-width, initial-scale=1'>\n"
                    f'\t\t<link rel="stylesheet" type="text/css" href="{self.stylesheet}">\n'
                    f"\t</head>\n"
                    f"\t<body>\n"
                    f"\t\t<p> <strong>Hello World></strong></p>\n"
                    f"\t</body>\n"
                    f"</html>"
                )

                self.assertEqual(html_content, expected_html_content)


# May have to run the 2 classes separately to make sure both conversions work. There might be a better way to do this.
if __name__ == "__main__":
    unittest.main()
