import fileinput
import sys
import os

filename = os.path.abspath(sys.argv[1])

urls = {
    '{10.1017/jog.2021.63}': '[10.1017/\ jog.2021.63]',
    '{10.5194/gmd-12-909-2019}': '[10.\ 5194/gmd-12-909-2019]',
    '{10.3189/2016AoG71A014}': '[10.3189/2016\ AoG71A014]',
    '{10.1007/s00704-014-1344-3}': '[10.1007/s00704-\ 014-1344-3]',
    '{10.1038/s41558-018-0093-1}': '[10.1038/s41558-\ 018-0093-1]',
    '%\setuppagenumbering[location={footer,center}]': '% Turn off page numbering as it is set in the footer\n\setuppagenumbering[location=]\n% Setup headers and footers\n\setupfootertexts[{\currentpage\ / \lastpage}]',
    'footer=0mm': 'footer=10mm',
}

print(f'Replacing {filename}')

for line in fileinput.input(filename, inplace=True):
    for k, v in urls.items():
        line = line.replace(k, v)
    print('{}'.format(line), end='')
