import re

# custom library
from frontmatter import process_md
# ---

def parse_md_inline_elements(html_contents):
    html_contents = re.sub(
        r"\[(.+?)\]\(([^ ]+)\)",  # Regex pattern to match .md link syntax and capture the text to display / the link
        r'<a href="\2">\1</a>',  # Replace all .md links with <a> tags with help from backreferences
        html_contents,
    )

    html_contents = re.sub(
        r"(`)(.*?)\1", r'<code class="inline-code">\2</code>', html_contents
    )  # Regex to spot code tag in Markdown and convert it to code in HTML

    # html_contents = re.sub(
    #     r"(`{3})(.*?)\1", r'<code class="block-code">\2</code>', html_contents
    # )  # Regex to spot code tag in Markdown and convert it to code in HTML

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

def get_code_block(html_content_lines:list[str,]):
    '''
    this function converts multiline code block into html.
    previously it was done by regex but it was not working properly
    '''
    html_content = ""
    block_end = 0
    for index, line in enumerate(html_content_lines):
        if '```' not in line:
            html_content += line + '\n'
        else:
            block_end = index
            break

    code = f'<pre><code class="block-code">{html_content}</code></pre>'

    return code, block_end  


def base_html_template(html_contents:str, metadata:dict)->str:
    """
    Base template of a html file
    """
    return f'''
<!DOCTYPE html>
<html>
<head>
<title>{metadata['title']}</title>
<meta name="description" content="{metadata['description']}" />
</head>
<body>{html_contents}</body>
<html>
'''

def write_to_html(output_file, html_contents, metadata):
    with open(output_file, "w") as html:
        html.write(base_html_template(html_contents, metadata))



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

def md_to_html(input_file, have_frontmatter:bool = True)->None:

    html_contents:str = ""
    index = 0
    lines:list[str] = []

    filename = input_file.split("\\")[-1]
    filename = filename.replace(".md", "")
    description = '''This web page is converted from a markdown file to html file using txt-to-HTML-converter python library. https://github.com/dshaw0004/txt-to-HTML-converter follow this url for more info'''
    metadata:dict = {
        'title': filename,
        'description': description
    }

    with open(input_file) as file:
        if have_frontmatter :
            data = file.read()
            frontmatter, content = process_md(data)
            metadata['title'] = frontmatter['title'] if frontmatter['title'] else filename
            metadata['description'] = frontmatter['description'] if frontmatter['description'] else description
            lines.extend(content.split("\n"))
        else:
            lines.extend(file.readlines())
    
    while index < len(lines):
        
        line = lines[index]
        index += 1
        if line.startswith("#"):
            line = change_to_heading(line)
        elif line.startswith("```"):
            line, skip_to = get_code_block(lines[index:])
            index = index + skip_to + 1 
    

        html_contents += line


    html_contents = parse_md_inline_elements(html_contents)

    write_to_html(input_file.replace(".md", ".html") ,html_contents, metadata)


if __name__ == "__main__":
    md_to_html(r"D:\PythonVENV\txt-to-HTML-converter\examples\ytdownloader_with_frontmatter.md", have_frontmatter=True)
