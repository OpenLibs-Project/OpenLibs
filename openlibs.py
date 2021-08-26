# This is final script for OpenLibs package manager

import os

from Ansi import Ansi
from Download import Download
from Interface import Interface

class Main:
    def __init__(self):
        self.opt_int = 0

    def chech_conditions(self):
        opt = self.opt_int
        if opt == 1:
            Download.download(None)

        elif opt == 2:
            print('opt is 2')
        elif opt == 3:
            print('opt is 3')

    def show(self):
        while True:
            options = ['Download a Package', 'View all packages', 'Update package List']
            output = Interface.cmenu(None, options)
            self.opt_int = output
            self.chech_conditions()

if __name__ == '__main__':
    os.system('clear')
    menu_object = Main()
    menu_object.show()


    
