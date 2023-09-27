import os
from shutil import rmtree



def remove_output_dir(
        output_dir):  # function to remove output directory if it exists and make a new one regardless of if it exists or not
    if os.path.exists(output_dir):
        rmtree(output_dir)  # using rmtree to delete the directory even if it has files in it

    os.makedirs(output_dir)  # Re/creating the output directory

def html_creator(input_file, stylesheet):

    html_header = (f"<!DOCTYPE html>\n"
                   f"<html lang='en'>\n"
                   f"\t<head>\n"
                   f"\t\t<meta charset='utf-8'>\n")  # Creating the start of the html file

    # Getting the file name and removing the path and txt extension, so it can be used in the title tag
    title = os.path.splitext(os.path.basename(input_file))[0]

    html_header += f"""\n \t\t<title>{title}</title>\n\t\t<meta name='viewport' content='width=device-width, initial-scale=1'> 
    \t{f'<link rel="stylesheet" type="text/css" href="{stylesheet}">'}
    \n\t</head>\n\t<body>\n"""

    return html_header


def generate_duplicate_filename(output_dir, output_file):
    count = 2
    generated_filename = output_file
    while (os.path.exists(generated_filename)):
        output_filename = os.path.splitext(os.path.basename(output_file))[0] + " (" + str(count) + ").html"
        generated_filename = os.path.join(output_dir, output_filename)
        count = count + 1

    return generated_filename