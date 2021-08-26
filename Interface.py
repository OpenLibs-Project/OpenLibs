from Ansi import Ansi

class Interface:
    def __init__(self):
        pass

    @staticmethod
    def cmenu(self, options):
        print()
        for option in range(len(options)):
            Ansi.cprint(f'[{option + 1}] ~ {options[option]}', 'green')
        while True:
            print()
            output = input('Option: ')
            try:
                output = int(output)
                if output > 0 and output < len(options) + 1:
                    return output
                else:
                    print()
                    Ansi.cprint('[-] ~ Invalid option ~ Out of range', 'red')
            except:
                print()
                Ansi.cprint('[-] ~ Invalid option ~ Has to be an integer', 'red')
