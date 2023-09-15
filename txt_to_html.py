import argparse
import os
from shutil import rmtree

VERSION = "0.1"


def remove_output_dir(
        output_dir):  # function to remove output directory if it exists and make a new one regardless of if it exists or not
    if os.path.exists(output_dir):
        rmtree(output_dir)  # using rmtree to delete the directory even if it has files in it

    os.makedirs(output_dir)  # Re/creating the output directory


def text_to_html(input_path, stylesheet, output_dir):
    try:
        if os.path.exists(input_path) and os.path.isdir(input_path):  # if the user inputted a directory
            remove_output_dir(output_dir)
            for filename in os.listdir(input_path):
                if filename.endswith(".txt"):
                    output_file = os.path.splitext(filename)[
                                      0] + ".html"  # creating the name of the output_file to have the name of the file currently being processed and end with .html
                    input_file = os.path.join(input_path, filename)
                    output_file = os.path.join(output_dir, output_file)

                    # opening the input file
                    with open(input_file, "r") as txt:
                        lines = txt.readlines()

                    html_contents = f"<html lang='en'>\n<head>\n\t<meta charset='utf-8'>\n"  # Creating the start of the html file

                    title = os.path.splitext(os.path.basename(input_file))[
                        0]  # Getting the file name and removing the path and txt extension so it can be used in the title tag
                    html_contents += f"""\n \t<title>{title}</title>\n\t<meta name='viewport' content='width=device-width, initial-scale=1'>{f'<link rel="stylesheet" type="text/css" href="{stylesheet}">'}
                    \n</head>\n<body>\n"""

                    in_paragraph = False  # Flag to track if we are inside a paragraph
                    for line in lines:
                        converted_line = line.strip()

                        if not in_paragraph:  # if in_paragraph is set to False, create the begining of the p tag in html_contnets and set in_paragraph to true
                            html_contents += "<p>"
                            in_paragraph = True

                        if line == "\n":  # if the current line is a newline close the p tag and append it to then set in_paragraph to False
                            html_contents += "</p>\n"
                            in_paragraph = False

                        else:  # if the code is still in a line with text and is in a paragraph append the line to html_contents
                            html_contents += f"{converted_line}"

                    # Closing the last paragraph if the loop was still in the paragraph when finished
                    if in_paragraph:
                        html_contents += "</p>\n"

                    html_contents += f"</body>\n</html>"

                    with open(output_file, "w") as html:
                        html.write(html_contents)

            print("File conversion was successful! Please look for the ", output_dir, " folder.")

        elif input_path.endswith(".txt") and os.path.isfile(input_path):
            remove_output_dir(output_dir)

            output_file = os.path.splitext(input_path)[
                              0] + ".html"  # creating the name of the output_file to have the name of the file currently being processed and end with .html
            input_file = input_path
            output_file = os.path.join(output_dir, output_file)

            with open(input_file, "r") as txt:
                lines = txt.readlines()

            html_contents = f"<html lang='en'>\n<head>\n\t<meta charset='utf-8'>\n"  # Creating the start of the html file
            title = os.path.splitext(os.path.basename(input_file))[0]  # Creating the title based off of the filename
            html_contents += f"""\n \t<title>{title}</title>\n\t<meta name='viewport' content='width=device-width, initial-scale=1'>{f'<link rel="stylesheet" type="text/css" href="{stylesheet}">'}
                                \n</head>\n<body>\n"""

            in_paragraph = False  # Flag to track if we are inside a paragraph
            for line in lines:
                converted_line = line.strip()

                if not in_paragraph:  # if in_paragraph is set to False, create the begining of the p tag in html_contnets and set in_paragraph to true
                    html_contents += "<p>"
                    in_paragraph = True

                if line == "\n":  # if the current line is a newline close the p tag and append it to then set in_paragraph to False
                    html_contents += "</p>\n"
                    in_paragraph = False

                else:  # if the code is still in a line with text and is in a paragraph append the line to html_contents
                    html_contents += f"{converted_line}"

            # Closing the last paragraph if the loop was still in the paragraph when finished
            if in_paragraph:
                html_contents += "</p>\n"

            html_contents += f"</body>\n</html>"

            with open(output_file, "w") as html:
                html.write(html_contents)
            print("File conversion was successful! Please look for the ", output_dir, " folder.")

        else:  # if the file/folder entered does not exist print this message
            print("The file/directory name does not exist. Please make sure you entered the correct name")

    except Exception as e:  # Throw an error if any kind of error happens
        print(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert a text file to an HTML file.",
                                     epilog="Example: python txt_to_html.py input.txt or python txt_to_html.py ./folder")

    parser.add_argument("--version", "-v", action="version", version=f"%(prog)s {VERSION}")

    parser.add_argument("input_path", help="Path to the input text file or directory")

    # Optional argument to use the stylesheet feature
    parser.add_argument("--stylesheet", "-s", metavar="<link>",
                        help="Use if you want to add a stylesheet to the generated HTML file")

    # Optional argument to use the output directory feature
    parser.add_argument("--output", "-o", metavar="<output_folder>",
                        help="Use if you want to change the destined output of the HTML files. Otherwise it will be sent to the til folder")

    args = parser.parse_args()

    input_path = args.input_path
    stylesheet = args.stylesheet
    output_dir = args.output or "./til"  # If the user does not enter an output directory, it will assign the directory til

    text_to_html(input_path, stylesheet, output_dir)
