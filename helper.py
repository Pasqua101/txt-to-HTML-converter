import os
import sys
from shutil import rmtree

from sidebar import table_of_contents


def remove_output_dir(
    output_dir,
):  # function to remove output directory if it exists and make a new one regardless of if it exists or not
    if os.path.exists(output_dir):
        rmtree(
            output_dir
        )  # using rmtree to delete the directory even if it has files in it

    os.makedirs(output_dir)  # Re/creating the output directory


def html_creator(input_file, stylesheet, lang, sidebar):
    generated_sidebar = generate_sidebar(sidebar) if sidebar is not None else None

    html_header = (
        f"<!DOCTYPE html>\n"
        f"""<html lang="{lang}">\n"""
        f"\t<head>\n"
        f"\t\t<meta charset='utf-8'>\n"
    )  # Creating the start of the html file

    # Getting the file name and removing the path and txt extension, so it can be used in the title tag
    title = os.path.splitext(os.path.basename(input_file))[0]

    html_header += f"""\n \t\t<title>{title}</title>\n\t\t
    \t<meta name='viewport' 
    \tcontent='width=device-width, 
    \tinitial-scale=1'> 
    \t{f'<link rel="stylesheet" type="text/css" href="{stylesheet}">'}
    \n\t</head>\n\t<body>\n"""

    if generated_sidebar is not None:
        html_header += f"{generated_sidebar} \n"

    return html_header


def generate_sidebar(sidebar):
    if os.path.isfile(
        sidebar
    ):  # while the code reads the table of contents directly from the sidebar file, we still have this check in case
        # the sidebar is removed
        sidebar_html = "\t\tTable of Contents\n\t\t<nav>\n\t\t\t<ul>\n"
        for item in table_of_contents:
            if "label" in item and "url" in item:
                sidebar_html += (
                    f'\t\t\t\t<li><a href="{item["url"]}">{item["label"]}</a></li>\n'
                )
        sidebar_html += "\t\t\t</ul>\n\t\t</nav>"
        return sidebar_html
    else:
        print("Sidebar must be a file or was not found")
        sys.exit(-1)


def generate_duplicate_filename(output_dir, output_file):
    count = 2
    generated_filename = output_file
    while os.path.exists(generated_filename):
        output_filename = (
            os.path.splitext(os.path.basename(output_file))[0]
            + " ("
            + str(count)
            + ").html"
        )
        generated_filename = os.path.join(output_dir, output_filename)
        count = count + 1

    return generated_filename


def extension_checker(filename):  # checks the extension name of files
    return filename.endswith((".txt", ".md"))


def output_file_creator(input_file, output_dir):
    try:
        output_file = (
            os.path.splitext(os.path.basename(input_file))[0] + ".html"
        )  # Constructing the output file's path based on the name of the input file
        output_file = os.path.join(output_dir, output_file)
        return output_file
    except Exception as e:
        raise Exception(f"Unable to create output file: {e}")
