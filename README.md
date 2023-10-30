# txt-to-HTML-converter
A conversion tool made for converting .txt and .md files to standard HTML.

The main purpose of this program is to create TIL (Today I learned) HTML files for blogging and personal purposes. A TIL can be pretty useful to anyone creating one as they can write down important things that they learned about and share it with others, or just keep it for themselves as something to reference. However, you can also use it as a simple .txt or .md  to HTML converter. 

# How to Use
This program is meant to be run on a CLI. First, make sure that you have the latest version of python installed. You can get the latest version from [here](https://www.python.org/downloads/). Once python is installed you can call on the program in your terminal or command line by doing so `python txt_to_html.py filename.txt` or `python txt_to_html.py foldername`. **Note**: Running this program will delete the output folder, so it can be recreated with updated files. So please make sure you are backing up any html files you may not want deleted in the specified output folder.

# Features

##  Customizing your Generated Files with a Stylesheet
If you wanted to spice up the look of your generated HTML file(s) you are able to add the stylesheet of your choice. To use simply do `python txt_to_html.py -s  https://cdnjs.cloudflare.com/ajax/libs/tufte-css/1.8.0/tufte.min.css filename.txt` or `python txt_to_html.py --stylesheet  https://cdnjs.cloudflare.com/ajax/libs/tufte-css/1.8.0/tufte.min.css filename.txt` into your command line. This also works with folders instead of a single .txt or .md file.

## Changing the Default Output Path to a Specified one
You can also set a different output path of your generated file(s). To use type `python txt_to_html.py -o .\foldername filename.txt` or `python txt_to_html.py --output .\foldername filename.txt` into your command line. This can also be done with folders instead of a single .txt or .md file.

## TOML file support
You can easily combine a multitude of arguments in one handy TOML file. To use, create a TOML file and add the arguments to it, then type `python txt_to_html.py -c filename.toml` or `python txt_to_html.py --config filename.toml` into your command line.

## Table of Contents (Preview)
You can create a table of contents with the sidebar.py file. To use, type `python txt_to_html.py -sb sidebar.py filename.txt` or `python txt_to_html.py --sidebar sidebar.py filename.txt`. Just make sure that in the sidebar.py you have updated the label and url to match the files you're generating (refer to the sidebar.py file to see the structure of the file). This argument also works with TOML config files. The feature is in a preview mode right now, as in the future I would like to try and update it with the ability to make a sidebar instead of just a table of contents.  

# Features Available Only in Markdown

## Customizing the lang attribute
If you're writing your HTML file in a different language, you can customize the lang attribute of the HTML tag by using the `-l` or `--lang` argument like so, `txt_to_html -l fr filename.txt`. If you don't use the argument, then by default the program will set the attribute to `en-CA` for Canadian English.
This program has the ability to detect Markdown code blocks and convert it the `<code>` tag in html. For example Markdown text that looks like this ``` `Hello World` ```, will show up like this `<code> Hello World </code>`.

## Horizontal Rule
If `---` is found in the Markdown file being converted. The program will convert it to the `<hr>` tag in HTML.

These features can all be used together. For example `python txt_to_html.py -o test -s https://cdnjs.cloudflare.com/ajax/libs/tufte-css/1.8.0/tufte.min.css .\filename.txt` or `python txt_to_html.py --output test --stylesheet https://cdnjs.cloudflare.com/ajax/libs/tufte-css/1.8.0/tufte.min.css .\filename.txt `.

## Detecting Code Blocks
This program has the ability to detect Markdown code blocks and convert it the `<code>` tag in html. For example Markdown text that looks like this ``` `Hello world` ```, will show up like this `<code>Hello world</code>` 

## Detecting Bold Markdown
The program is able to spot the use of bold Markdown. For example, this line `**Hello world**` would be converted to `<strong> Hello world </strong>` in HTML.

### Additional Terminal Commands

**Version** - To see the current version of the program you are running, type `python txt_to_html.py -v` or `python txt_to_html.py --version` into your command line.

**Help** - If you need additional help or a guide, you can type `python txt_to_html.py -h` or `python txt_to_html.py --help` into your command line.
