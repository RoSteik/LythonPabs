""" 
Created by RoSteik (Telegram: @Rosteik)
"""
import re as regex
import zipfile

if __name__ == '__main__':
    lines_list_with_regex = list()

    file_zip = zipfile.ZipFile('server.log (2).zip', 'r')
    file_zip.extractall('./')
    file_zip.close()

    with open('server.log (2).2018-04-04') as file:
        lines_list_from_file = [line.rstrip() for line in file.readlines()]

    for line in lines_list_from_file:
        line_to_find = regex.findall("INFO.*WFLY.*", line)

        if line_to_find:
            lines_list_with_regex.append(line_to_find)

    for matched_line in lines_list_with_regex:
        print(matched_line)
