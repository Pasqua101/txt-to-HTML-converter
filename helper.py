import re

def parse_md(html_contents):
    return re.sub(
    r'\[(.+?)\]\(([^ ]+)\)', # Regex pattern to match .md link syntax and capture the text to display / the link
    r'<a href=\2>\1</a>', # Replace all .md links with <a> tags with help from backreferences
    html_contents)