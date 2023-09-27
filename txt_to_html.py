import argparse
from file_processors import text_to_html

VERSION = "0.1"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert a text or markdown file to an HTML file.",
                                     epilog="Example: python txt_to_html.py input.txt or python txt_to_html.py ./folder")

    parser.add_argument("--version", "-v", action="version", version=f"%(prog)s {VERSION}")

    parser.add_argument("input_path", help="Path to the input file or directory")

    # Optional argument to use the stylesheet feature
    parser.add_argument("--stylesheet", "-s", metavar="<link>",
                        help="Use if you want to add a stylesheet to the generated HTML file")

    # Optional argument to use the output directory feature
    parser.add_argument("--output", "-o", metavar="<output_folder>",
                        help="Use if you want to change the destined output of the HTML files. Otherwise it will be sent to the til folder")

    # Optional argument to modify the lang attribute
    parser.add_argument("--lang", "-l", metavar="<lang attribute>",
                        help="Use if you want to indicate what language the input file is using for the HTML doc that will be generated")

    args = parser.parse_args()

    input_path = args.input_path
    stylesheet = args.stylesheet
    output_dir = args.output or "./til"  # If the user does not enter an output directory, it will assign the directory til
    lang = args.lang or "en-CA"

    text_to_html(input_path, stylesheet, output_dir, lang)
