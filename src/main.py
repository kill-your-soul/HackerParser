import os
from pathlib import Path
from colorama import Fore
from XakerParser import XakerParser

def main():
    try:
        login = os.environ['LOGIN']
        password = os.environ['PASSWORD']
    except KeyError:
        print(
            Fore.RED
            + "password or login not found in environment variables"
            + Fore.RESET
        )
        login = str(input("Input login for xakep.ru: "))
        password = str(input("Input password for xakep.ru: "))

    downloader = XakerParser(login, password, Path.cwd() / 'pdfs')
    downloader.parse_site()


if __name__ == '__main__':
    main()