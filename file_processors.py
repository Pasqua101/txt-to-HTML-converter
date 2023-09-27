from helper import *
import os
import re


def text_to_html(input_path, stylesheet, output_dir, lang):
    try:
        extension_check = input_path.endswith((".txt", ".md"))
        if os.path.exists(input_path) and os.path.isdir(input_path):  # if the user inputted a directory
            remove_output_dir(output_dir)
            for filename in os.listdir(input_path):
                if filename.endswith(".txt") or filename.endswith(".md"):

                    input_file = os.path.join(input_path, filename)
                    output_file = os.path.splitext(os.path.basename(input_file))[
                                      0] + ".html"  # Constructing the output file's path based on the name of the input file
                    output_file = os.path.join(output_dir, output_file)

                    if os.path.exists(output_file):
                        output_file = generate_duplicate_filename(output_dir, output_file)

                    html_contents = html_processor(input_file, stylesheet, lang)

                    if extension_check:
                        html_contents = parse_md(html_contents)

                    with open(output_file, "w") as html:
                        html.write(html_contents)

            print("File conversion was successful! Please look for the ", output_dir, " folder.")

        elif extension_check and os.path.isfile(input_path):
            remove_output_dir(output_dir)

            # Constructing the output file's path based on the name of the input file
            output_file = os.path.splitext(os.path.basename(input_path))[0] + ".html"
            output_file = os.path.join(output_dir, output_file)
            input_file = input_path

            html_contents = html_processor(input_file, stylesheet, lang)

            if extension_check:
                html_contents = parse_md(html_contents)

            with open(output_file, "w") as html:
                html.write(html_contents)
            print("File conversion was successful! Please look for the ", output_dir, " folder.")

        else:  # if the file/folder entered does not exist print error message
            print("The file/directory name does not exist. Please make sure you entered the correct name")

    except Exception as e:  # Throw an error if any kind of error happens
        print(f"An error occurred: {str(e)}")


def parse_md(html_contents):

    html_contents = re.sub(
        r'\[(.+?)\]\(([^ ]+)\)', # Regex pattern to match .md link syntax and capture the text to display / the link
        r'<a href=\2>\1</a>', # Replace all .md links with <a> tags with help from backreferences
        html_contents)

    html_contents = re.sub(r"(`{1,3})(.*?)\1", r"<code>\2</code>", html_contents)

    return html_contents

def html_processor(input_file, stylesheet, lang):

    html_contents = html_creator(input_file, stylesheet, lang)

    with open(input_file, "r") as txt:
        lines = txt.readlines()

    in_paragraph = False  # Flag to track if we are inside a paragraph
    for line in lines:
        converted_line = line
        if not in_paragraph:  # if in_paragraph is set to False, create the begining of the p tag in html_contnets and set in_paragraph to true
            html_contents += "\t\t<p>"
            in_paragraph = True
        if line == "\n":  # if the current line is a newline close the p tag and append it to then set in_paragraph to False
            html_contents += "</p>\n"
            in_paragraph = False
        else:  # if the code is still in a line with text and is in a paragraph append the line to html_contents
            converted_line = line.replace("\n", "")
            html_contents += f" {converted_line}"
    # Closing the last paragraph if the loop was still in the paragraph when finished
    if in_paragraph:
        html_contents += "</p>\n"

    html_contents += f"\t</body>\n</html>"

    return html_contents