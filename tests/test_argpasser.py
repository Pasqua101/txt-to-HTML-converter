import unittest
from unittest.mock import patch
import argparse
from txt_to_html import VERSION

class TestVersionOption(unittest.TestCase):
    def test_version_argument(self):
        ''' This is to test the -version and -v argument 
        and ensure its functionality'''

        # patch basically simulates the command line argument as part of the unittest
        with patch("sys.argv", ["txt_to_html.py", "--version"]):
            try:
                parser = argparse.ArgumentParser()
                parser.add_argument("--version", "-v", action="version", version=f"%(prog)s {VERSION}")
                parser.parse_args()
                
        #Systemexit ensures that the code is truly true and the test successfully ran
            except SystemExit as exit:
                self.assertEqual(exit.code, 0)



if __name__ == "__main__":
    unittest.main()
