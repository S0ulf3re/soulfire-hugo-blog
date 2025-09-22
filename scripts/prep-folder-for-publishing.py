import sys
import os
import argparse
import glob
import markdown
import re 
from datetime import datetime
parser = argparse.ArgumentParser(description='folder path from Shortcuts')
parser.add_argument("--file-path", type=str, default="")
args = parser.parse_args()

file_path = os.path.normpath(args.file_path)

# Get markdown file
md_files = file_path

if not md_files:
    print("No Markdown files found")
    exit(1)

# Get the title of the markdown file
md_file = md_files
md_file_title = ""
with open(md_file, "r", encoding="utf-8") as input_file:
    text = input_file.read()
    html = markdown.markdown(text)
    try:
        md_file_title = re.search("<h1>(.*?)</h1>", html).group(1)
    except AttributeError:
        print("No title found")
        exit(1)
    
    input_file.close()

# Assemble the Hugo data
hugo_header = "---\n" \
"title: " + md_file_title + "\n" \
"date: " + datetime.today().strftime('%Y-%m-%d') + "\n" \
"---\n"

# Remove the h1 title and add the Hugo data
with open(md_file, 'r') as file_input:
    data = file_input.read().splitlines(True)
    data.pop(0)
with open(md_file, 'w') as file_output:
    file_output.write(hugo_header)
    file_output.writelines(data)
    file_output.close()




