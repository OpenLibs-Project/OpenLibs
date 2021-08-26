class Ansi:
    @staticmethod
    def cprint(content, color) -> int:
        color_dict = {
            'green': '82',
            'dark-green': '149',
            'red': '196',
            'orange': '208',
            'white': '15'
        }
        toprint = '\033[38;5;' + color_dict[color] + 'm' + content + '\033[m'
        lastcontent = content[-11:]
        if lastcontent == '/notnewline':
            print('\033[38;5;' + color_dict[color] + 'm' + content[:-11] + '\033[m', end=' ')
        else:
            print(toprint)
        return 0