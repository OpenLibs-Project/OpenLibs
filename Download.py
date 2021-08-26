import os
import requests
import subprocess

from Ansi import Ansi

class Download:
    @staticmethod
    def download(self) -> bool:
        while True:
            print()
            Ansi.cprint('Package Name: /notnewline', 'green')
            name = input()
            print()
            Ansi.cprint('Processing URL...', 'green')
            print()
            url = 'https://github.com/OpenLibs-Project/' + name
            response = requests.get(url)
            if response.status_code > 199 and response.status_code < 201:
                exists = True
                break
            else:
                Ansi.cprint('[-] ~ Invalid package name ~ Repository does not exist', 'red')
                exists = False
        if exists:
            while True:
                Ansi.cprint('Download path (Blank = current): /notnewline', 'green')
                download_path = input()
                if os.path.isdir(download_path) or download_path == '':
                    print()
                    Ansi.cprint('[+] ~ Downloading package repository', 'green')
                    print()
                    try:
                        os.system(f'git clone {url}')
                    except:
                        Ansi.cprint(f'[-] ~ An error ocurred while downloading ~ Try removing any folders with name: {name}', 'red')
                    print()
                    if download_path != '':
                        os.system(f'mv {name} {download_path}')
                    break
                else:
                    Ansi.cprint('[-] ~ Invalid directory ~ Does not exist', 'red')

