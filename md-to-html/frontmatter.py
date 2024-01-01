



def extractData(data: str):
	
	matches = data.split("---")
	if not matches:
		return "no frontmatter exit", data
	frontmatter = formatFrontMatter(matches[1])
	# print(frontmatter)
	return frontmatter, matches[2]




def formatFrontMatter(data: str):
	frontMatter: dict = {}
	frontMatterTextArray = data.split("\n")
	# print(data)
	frontMatterTextArray = [seg for seg in frontMatterTextArray if seg]
	for d in frontMatterTextArray:
		newText = d.replace(" ", "")
		newTextArray = newText.split(":")
		frontMatter[newTextArray[0]] = newTextArray[1].replace('"', "")
		
	return frontMatter




def process_md(file_data):
	frontmatter, content = extractData(file_data)
	return frontmatter, content
