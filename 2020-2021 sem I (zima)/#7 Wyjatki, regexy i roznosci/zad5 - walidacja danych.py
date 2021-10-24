# Created by Marcin "Cozoob" Kozub 24.10.2021
import re

# validation - version alpha
def val_v_alpha(first_name, last_name, email):
    try:
        first_name = re.search(r"[A-Za-z]+", first_name).group()
        last_name = re.search(r"[A-Za-z]+", last_name).group()
        email = re.search(r"\w*@\w*\.[a-zA-Z][a-zA-Z]+", email).group()
    except AttributeError:
        return "Invalid input!"
    return first_name.capitalize(), last_name.capitalize(), email

# validation - version beta
def val_v_beta(first_name, last_name, email):
    try:
        first_name = re.search(r"[A-Za-z]+", first_name).group()
        last_name = re.search(r"[A-Z\-a-z]+", last_name).group()
        email = re.search(r"[\w\W]*@[\w\W]*\.[a-zA-Z][a-zA-Z]+", email).group()
    except AttributeError:
        return "Invalid input!"
    return first_name.capitalize(), last_name.capitalize(), email


if __name__ == '__main__':
    # testing val_v_alpha
    print(val_v_alpha(" Marcin -", " kOzub3", "jurij76@ok.com"))
    print(val_v_alpha(" Marcin -", " kOzub3", "jurij76ok.com"))
    print(val_v_alpha(" Marcin -", " kOzub3", "jurij76@ok.c"))

    # testing val_v_beta
    print(val_v_beta(" Marcin -", " kOzub-heinz3", "jurij76@ok.com"))
    print(val_v_beta(" Marcin -", " kOzub3", "jurij-76@ok.com"))
    print(val_v_beta(" Marcin -", " kOzub3", "jurij76@o_k.com"))