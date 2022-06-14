# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import pandas as pd
import subprocess
import os
import re

# from nanoid import generate

try:
    from pybtex.database import parse_file
except:
    os.system('pip install pybtex')
    from pybtex.database import parse_file

# def process_bibtex(fn):
#     with open(fn, encoding='utf-8') as r_file:
#         bibtex = r_file.read()
#     pattern = r"@([aA]+?){([wW0-9_-]+?),"
#
#     def callback(matchobj):
#         return f"@{matchobj.group(1)}{{{generate()},"
#
#     with open(fn, 'w', encoding="utf-8") as w_file:
#         w_file.write(re.sub(pattern, callback, bibtex))
from nanoid import generate


def process_bibtex(fn):
    with open(fn, encoding="utf-8") as r_file:
        bibtex = r_file.read()
    pattern = r"@([\w\W]+?){([\w\W0-9_\-]+?),"
    def callback(matchobj):
        return f"@{matchobj.group(1)}{{{generate('1234567890abcdefghijklmnopqrstuvz')},"
    with open(fn, "w", encoding="utf-8") as w_file:
        w_file.write(re.sub(pattern, callback, bibtex))


def main():
    inFile = sys.argv[1]
    outFile = sys.argv[2]
    # csv0 = open(inFile, 'r')
    # print(csv0.read())

    df = pd.read_csv(inFile)
    try:
        DOI_list = df[['DOI']]
    except:
        DOI_list = 0, df.iloc[:, 0]

    missingDOIs = df[DOI_list.isna()]
    num_missingDOIs = len(missingDOIs)
    print(num_missingDOIs)
    # print(missingDOIs)

    print(DOI_list)
    num_DOIs = len(DOI_list)
    # txt0 = open(outFile, 'w')
    # txt0.write(DOI_list)
    # txt0.close()

    DOI_list.to_csv(outFile, header=None, index=None, sep='\n')

    subprocess.run("doi2bib --input /home/jasjiang/PycharmProjects/doibibtex/output.txt --output "
                   "/home/jasjiang/PycharmProjects/doibibtex/refs_cce.bib", shell=True)

    # process_bibtex("/home/jasjiang/PycharmProjects/doibibtex/refs.bib")
    # throwing errors because of duplicate keys
    # bib_data = parse_file('refs.bib')
    # num_entries = 0
    # for doi in bib_data.entries:
    #     num_entries = num_entries + 1
    #
    # if num_entries != num_DOIs:
    #     print('doi2bib missing entries')
    # else:
    #     print('successfully outputted bibtex, please check for full names')


# csv_file = raw_input(csv)
# txt_file = raw_input(txt0)

#
# def bib_to_txt(name):
#     # Use a breakpoint in the code line below to debug your script.
# 	bibfile = parse_file(bibfile)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    process_bibtex("/home/jasjiang/PycharmProjects/doibibtex/refs_cce.bib")

