""" 
Created by RoSteik (Telegram: @Rosteik)
"""

import re as regex
import zipfile


def extract_info_from_zipfile():
    lines_list_with_regex = list()

    zipfile_name = 'server.log (2).zip'
    file_zip = zipfile.ZipFile(zipfile_name, 'r')
    file_zip.extractall('./')
    file_zip.close()

    file_name_from_zip = 'server.log (2).2018-04-04'

    with open(file_name_from_zip) as file:
        lines_list_from_file = [line.rstrip() for line in file.readlines()]

    for line in lines_list_from_file:
        line_to_find = regex.findall(r"INFO\s+\[.*wildfly.*].*WFLY.*", line)
        if line_to_find:
            lines_list_with_regex.append(line_to_find)

    for matched_line in lines_list_with_regex:
        print(matched_line)
