# Created by Marcin "Cozoob" Kozub 02.11.2021
from bs4 import BeautifulSoup

def select_links(html):
    with open(html, "r") as file:
        soup = BeautifulSoup(file, "html.parser")
    return soup.find_all("a")

if __name__ == '__main__':
    print(select_links("converted_file.html"))