import fileinput
import sys
import os

filename = os.path.abspath(sys.argv[1])

def replace_head_tag(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Replace the </head> tag with the script and the closing </head>
    new_lines = []
    for line in lines:
        if line.strip() == '</head>':
            new_lines.append('<script defer="" data-domain="fabienmaussion.info" src="https://plausible.io/js/script.js"></script>\n')
            new_lines.append('</head>\n')
        else:
            new_lines.append(line)

    # Write the changes back to the file
    with open(file_path, 'w') as file:
        file.writelines(new_lines)

# Usage
replace_head_tag(filename)
