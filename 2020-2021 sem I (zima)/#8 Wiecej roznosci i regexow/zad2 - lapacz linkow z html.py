# Created by Marcin "Cozoob" Kozub 01.11.2021
import re

def select_links(html):
    answer = []
    with open(html, "r") as file:
        for line in file:
            try:
                matched_line = re.search(r"(?=<a)[^=]+?href=\"(?P<link>[^'=]*?)\"[^href]*?>(?P<text>.*?)</a>", line)
                answer.append(matched_line.groupdict())
            except AttributeError:
                pass

    return answer

if __name__ == '__main__':

    print(select_links("converted_file.html"))