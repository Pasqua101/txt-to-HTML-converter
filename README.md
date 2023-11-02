[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# TXT to HTML Converter
A conversion tool made for converting .txt and .md files to standard HTML.

The main purpose of this program is to create TIL (Today I learned) HTML files for blogging and personal purposes. A TIL can be pretty useful to anyone creating one as they can write down important things that they learned about and share it with others, or just keep it for themselves as something to reference. However, you can also use it as a simple .txt or .md  to HTML converter. For setup look at the setup section in the CONTRIBUTING.md file.

### Table of Contents
 - [Features](#features)
 - [Optional Arguments](#optional-arguments)
 - [Usage](#usage)

# Features
 - Users can specify a file or folder containing md or txt files for HTML conversion.
 - A stylesheet is added by default to the generated files.
 - TOML file support.
 - Markdown Only Features:
   - Detecting and converting code blocks to HTML `<code>` tag.
   - Detecting and converting bold Markdown syntax to HTML `<strong>` tag.
   - Detecting and converting horizontal rule Markdown syntax to HTML `<hr>` tag.

## Optional Arguments

| Argument                                  | Purpose                                                                                                       |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| -s, --stylesheet <CSS stylesheet URL>     | Changes the default CSS stylesheet provided for the generated files                                           |
| -l, --lang <lang attribute>               | Specifies language used when generating HTML files. If not used, the default will be en-CA                    |
| -c, --config <path to config.toml file>   | Allows for multiple arguments to be used at once, without having to type it all into a CLI                    |
| -o, --output <foldername>                 | Specifies a different output directory for the generated HTML files, instead of the default TIL directory     |
| -sb, --sidebar <path to siderbar.py file> | Currently in preview, but generates a table of contents for you based on the already provided sidebar.py file |
| -v, --version                             | Displays program name and current versions                                                                    |
| -h, --help                                | Provides help on the CLI explaining arguments and shows an example of execution                               |

## Usage
Customizing the Stylesheet

`python txt_to_html.py -s  https://cdnjs.cloudflare.com/ajax/libs/tufte-css/1.8.0/tufte.min.css filename.txt` or `python txt_to_html.py --stylesheet  https://cdnjs.cloudflare.com/ajax/libs/tufte-css/1.8.0/tufte.min.css filename.txt`

Changing the output directory

`python txt_to_html.py -o .\foldername filename.txt` or `python txt_to_html.py --output .\foldername filename.txt` 

Using a TOML config file

`python txt_to_html.py -c filename.toml` or `python txt_to_html.py --config filename.toml`

Generating a table of contents (sidebar)

`python txt_to_html.py -sb sidebar.py filename.txt` or `python txt_to_html.py --sidebar sidebar.py filename.txt`

Changing the lang attribute

`python txt_to_html -l fr filename.txt` or `python txt_to_html --lang fr filename.txt`


All the examples above can be used together on the CLI or in a TOML config file. 

Checking the version of TXT to HTML Converter

`python txt_to_html.py -v` or `python txt_to_html.py --version`

Getting help for TXT to HTML Converter

`python txt_to_html.py -h` or `python txt_to_html.py --help`


Example output of the program can be found in the examples folder.