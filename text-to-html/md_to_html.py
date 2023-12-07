import re

def parse_md_inline_elements(html_contents):
    html_contents = re.sub(
        r"\[(.+?)\]\(([^ ]+)\)",  # Regex pattern to match .md link syntax and capture the text to display / the link
        r"<a href=\2>\1</a>",  # Replace all .md links with <a> tags with help from backreferences
        html_contents,
    )

    html_contents = re.sub(
        r"(`{1,3})(.*?)\1", r"<code>\2</code>", html_contents
    )  # Regex to spot code tag in Markdown and convert it to code in HTML

    html_contents = re.sub(
        r"---+", r"<hr>", html_contents
    )  # Regex to spot horizontal rule in Markdown and convert it to HTML

    html_contents = re.sub(
        r"\*\*(.*?)\*\*", r"<strong>\1</strong>", html_contents
    )  # Regex to spot bold in Markdown and convert the text inside it (group 1) to HTML
    
    html_contents = re.sub(
        r"\*(.*?)\*", r"<em>\1</em>", html_contents
    )  # Regex to spot italic in Markdown and convert the text inside it (group 1) to HTML

    return html_contents

def base_html_template(html_contents:str)->str:
    """
    Base template of a html file
    """
    return f'''
<!DOCTYPE html>
<html>
<head>
<title>md to html</title>
</head>
<body>{html_contents}</body>
<html>
'''

def change_to_heading(heading:str)-> str:
    """
    it changes markdown headings to html headings
    """
    init_len = len(heading)
    heading = re.sub(r'^#+',"", heading)
    final_len = len(heading)
    heading_level = init_len - final_len if (init_len - final_len) <= 6 else 6
    heading = heading.strip("\n")
    return f"<h{heading_level}>{heading.strip(' ')}</h{heading_level}>"

def md_to_html(input_file):

    with open(input_file) as file:
        lines = file.readlines()

    html_contents:str = ""

    for line in lines:
        if line.startswith("#"):
            line = change_to_heading(line)
        html_contents += line

    html_contents = parse_md_inline_elements(html_contents)

    return html_contents