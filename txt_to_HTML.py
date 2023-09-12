import \
    argparse  # using argparse allows us to properly take in arguments from the command line, and even accept things like --help or --version
import os  # importing os to allow us to create a new directory on the system and walk into a directory
from shutil import  rmtree # importing rmtree from shutil to allow us to move the output file to the til directory and delete the til directory

VERSION = "0.1"  # This will be returned when the user types in --version or -v


def remove_output_dir(output_dir): # function to remove output directory if it exists and make a new one regardless of if it exists or not
    if os.path.exists(
            output_dir):  # Checking to see if the folder already exists, because if it does the program will not be able to write to the file
        rmtree(
            output_dir)  # The os library does have a rmdir function, but it will not delete the directory if it isn't empty.
        # Since we're just recreating the directory each time the program is ran. rmtree will solve this problem by deleting everything in the requested folder

    os.makedirs(output_dir)  # Doesn't need an else statement, as we'll need to create a new directory no matter what


def text_to_html(input_path, stylesheet, output_dir):
    try:


        html_header = f"<html lang='en'>\n<head>\n\t<meta charset='utf-8'>\n"  # Writing the first part of the html file

        if os.path.exists(input_path) and os.path.isdir(input_path):  # if the user inputted a directory then convert all the txt files to html:
            remove_output_dir(output_dir)

            for filename in os.listdir(input_path):
                if filename.endswith(".txt"):  #
                    output_file = os.path.splitext(filename)[0] + ".html"
                    input_file = os.path.join(input_path, filename)
                    output_file = os.path.join(output_dir, output_file)

                    # opening the input file
                    with open(input_file, "r") as txt:
                        lines = txt.readlines()


                    html_contents = html_header
                    title = os.path.splitext(os.path.basename(input_file))[
                        0]  # Creating the title based off of the filename
                    html_contents += f"""\n \t<title>{title}</title>\n\t<meta name='viewport' content='width=device-width, initial-scale=1'>{f'<link rel="stylesheet" type="text/css" href="{stylesheet}">'}
                    \n</head>\n<body>\n"""

                    for line in lines:
                        if line == "\n":  # If there is a new line in the txt file, add the <br> tag
                            html_contents += f"<br>\n"
                        else:  # Otherwise add the <p> tag to the line
                            converted_line = line.replace("\n",
                                                          "")  # Removing the newline terminator at the line of the line to help make the html formatting clearer to read
                            html_contents += f"<p>{converted_line}</p>\n"

                    html_contents += f"</body>\n</html>"  # Adding in the closing part of the HTML

                    with open(output_file, "w") as html:
                        html.write(html_contents)

                print("File conversion was successful! Please look for the ", output_dir ," folder.")

        elif input_path.endswith(".txt") and os.path.isfile(input_path):
            remove_output_dir(output_dir)

            output_file = os.path.splitext(input_path)[0] + ".html"
            input_file = input_path
            output_file = os.path.join(output_dir, output_file)

            # Opening the input file for reading
            with open(input_file, "r") as txt:
                lines = txt.readlines()


            html_contents = html_header
            title = os.path.splitext(os.path.basename(input_file))[0]  # Creating the title based off of the filename
            html_contents += f"""\n \t<title>{title}</title>\n\t<meta name='viewport' content='width=device-width, initial-scale=1'>{f'<link rel="stylesheet" type="text/css" href="{stylesheet}">'}
                                \n</head>\n<body>\n"""

            for line in lines:
                if line == "\n":
                    html_contents += f"<br>"
                else:
                    converted_line = line.replace("\n", "")
                    html_contents += f"<p>{converted_line}</p>\n"

            html_contents += f"</body>\n</html>"

            with open(output_file, "w") as html:
                html.write(html_contents)
            print("File conversion was successful! Please look for the ", output_dir, " folder.")
        else:
            print("The file/directory name does not exist. Please make sure you entered the correct name")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    # NOTE: Description allows for a description of the program to show up when -h or --help is entered
    # NOTE: epilog allows for us to provide the user with an example of how to call on/run the program
    parser = argparse.ArgumentParser(description="Convert a text file to an HTML file.",
                                     epilog="Example: python main.py input.txt or python main.py ./folder")
    parser.add_argument("input_path",
                        help="Path to the input text file or directory")  # The help keyword on this line and the line below  will allow the program to show the user the argument that is needed to run the program

    # Line of code below will allow a --version or -v to work
    parser.add_argument("--version", "-v", action="version", version=f"%(prog)s {VERSION}")

    #optional feature 1
    parser.add_argument("--stylesheet", "-s", help="Use if you want to add a stylesheet to the generated HTML file")

    #optional feature 2
    parser.add_argument("--output", "-o", help="Use if you want to change the destined output of the HTML files. Otherwise it will be sent to the til folder")

    args = parser.parse_args()
    input_path = args.input_path
    stylesheet = args.stylesheet
    output_dir = args.output or "./til"

    text_to_html(input_path, stylesheet, output_dir)
