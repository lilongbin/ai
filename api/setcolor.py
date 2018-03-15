import colorama
colorama.init(autoreset=True)

def setcolor(msg, color='blue'):
    color_value = eval("colorama.Fore.%s" % color.upper())
    msg = colorama.Style.RESET_ALL + color_value + msg
    return msg

def test():
    for color in ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']:
        print("color %s: %s" % (color, setcolor(color, color)))

if __name__ == '__main__':
    test()
