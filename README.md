# txt-to-HTML-converter
A conversion tool made for converting .txt and .md files to standard HTML.

The main purpose of this program is to create TIL (Today I learned) HTML files for blogging and personal purposes. A TIL can be pretty useful to anyone creating one as they can write down important things that they learned about and share it with others, or just keep it for themselves as something to reference. However, you can also use it as a simple txt to HTML converter. 

# How to Use
This program is meant to be run on a CLI. First, make sure that you have the lastest version of python installed. You can get the latest version from [here](https://www.python.org/downloads/). Once python is installed you can call on the program in your terminal or command line by doing so `python txt_to_html.py filename.txt` or `python txt_to_html.py foldername`. **Note**: Running this program will delete the output folder so it can be recreated with updated files. So please make sure you are backing up any html files you may not want deleted in the specified output folder.

# Features

##  Customizing your Generated Files with a Stylesheet
If you wanted to spice up the look of your generated HTML file(s) you are able to add the stylesheet of your choice. To use simply do `txt_to_html -s  https://cdnjs.cloudflare.com/ajax/libs/tufte-css/1.8.0/tufte.min.css filename.txt` or `txt_to_html --stylesheet  https://cdnjs.cloudflare.com/ajax/libs/tufte-css/1.8.0/tufte.min.css filename.txt` into your command line. This also works with folders instead of a single txt file.

## Changinging the Default Output Path to a Specified one
You can also set a different output path of your generated file(s). To use type `txt_to_html -o .\foldername filename.txt` or `txt_to_html --output .\foldername filename.txt` into your command line. This can also be done with folders instead of a single txt file.

These features can all be used together. For example `txt_to_html -o test -s https://cdnjs.cloudflare.com/ajax/libs/tufte-css/1.8.0/tufte.min.css .\filename.txt` or `txt_to_html --output test --stylesheet https://cdnjs.cloudflare.com/ajax/libs/tufte-css/1.8.0/tufte.min.css .\filename.txt `.

# Markdown Features

## Detecting Code Blocks
The program is able to detect Markdown Code blocks like ``` `Hello World` ``` and convert to `<code> Hello World </code>` in HTML. 

### Additional Terminal Commands

**Version** - To see the current version of the program you are running, type `txt_to_html -v` or `txt_tom_html --version` into your command line.

**Help** - If you need additional help or a guide, you can type `txt_to_html -h` or `txt_to_html --help` into your command line.
