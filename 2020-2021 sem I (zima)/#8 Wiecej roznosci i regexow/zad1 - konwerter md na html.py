# Created by Marcin "Cozoob" Kozub 30.10.2021
import re

def md_to_html(string):
    # searching for links to convert to href
    try:
        elem = re.search(r"(?<!!)\[(.*?)\]\((.*?)\)", string)
    except AttributeError:
        elem = None

    if elem:
        return elem, "link"

    # searching for headers to convert to h1
    try:
        elem = re.search(r"(?<=# ).+", string)
    except AttributeError:
        elem = None

    if elem:
        return elem, "header"

    # searching for blockquote to convert to <cite>...</cite>
    try:
        elem = re.search(r"(?=<).+(?<=>)", string)
    except AttributeError:
        elem = None

    if elem:
        return elem, "blockquote"
    # searching for bold text to convert to <b>...</b>
    try:
        elem = re.search(r"(?=\*\*).+(?<=\*\*)", string)
    except AttributeError:
        elem = None

    return elem, "boldtext"


def convert_file(file_to_conv):
    # change to dict afterwards and convert to html standard
    answer = []
    with open(file_to_conv, "r") as file:
        for line in file:
            elem = md_to_html(line)
            key = elem[1]
            if line == "\n":
                new_line = "<br>"
            elif key == "link":
                start, end = elem[0].span()
                name, link = elem[0].group(1, 2)
                new_line = line[0:start] + '<a href=\"' + link + "\">" + name + "</a><br>" + line[end:len(line)].strip()
            elif key == "header":
                text = elem[0].group()
                new_line = "<h1>" + text + "</h1><br>" + line[end:len(line)].strip()
            elif key == "blockquote":
                start, end = elem[0].span()
                text = elem[0].group()
                new_line = line[0: start] + "<cite>" + text[1:len(text) - 1] + "</cite>" + line[end: len(line) - 2] \
                           + "<br>"

            elif key == "boldtext":
                start, end = elem[0].span()
                text = elem[0].group()
                new_line = line[0: start] + "<b>" + text[2: len(text) - 2] + "</b>" + line[end:len(line) - 2] + "<br>"
            else:
                new_line = line + "<br>"

            answer.append(new_line)

    with open("converted_file.html", "w") as conv_file:
        for line in answer:
            conv_file.write(line + "\n")


if __name__ == '__main__':

    convert_file("zad1test.txt")