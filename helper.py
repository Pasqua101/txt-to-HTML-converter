import os
import re

def parse_md(html_contents):
    return re.sub(
    r'\[(.+?)\]\(([^ ]+)\)', # Regex pattern to match .md link syntax and capture the text to display / the link
    r'<a href=\2>\1</a>', # Replace all .md links with <a> tags with help from backreferences
    html_contents)

def generate_duplicate_filename(output_dir, output_file):
    count = 2
    while (os.path.exists(output_file)):
        output_filename = os.path.splitext(os.path.basename(output_file))[0] + " (" + str(count) + ").html" 
        output_file = os.path.join(output_dir, output_filename)
        count = count + 1
    
    return output_file