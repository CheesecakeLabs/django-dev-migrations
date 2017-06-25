STYLES = {
    'RED': '\033[1;31m',
    'BLUE': '\033[1;34m',
    'GREEN': '\033[0;32m',
    'RESET': '\033[0;0m',
    'BOLD': '\033[;1m',
}


def print_color(text, color):
    color_code = STYLES.get(color)
    print(color_code, end='')
    print(text)
    print(STYLES['RESET'], end='')