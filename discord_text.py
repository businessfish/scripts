from tkinter import Tk

###
### convert a given string to the big letter emojis in discord and send it to the clipboard.
###
def convert(str):
    str = str.lower()
    out_str= ''
    for c in str:
        if c != ' ' and not c.isdigit() and c != '!' and c != '.' and c != ',' and c != '?':
            out_str += (':regional_indicator_' + c + ':' + ' ')
        elif c == ' ':
            out_str += '   '
        elif c == '?':
            out_str += ':grey_question: '
        elif c == '!':
            out_str += ':grey_exclamation: '
        elif c == '.':
            out_str += '. '
        elif c == ',':
            out_str += ', '
        elif c,isdigit():
            if c == '1':
                out_str += ':one: '
            elif c == '2':
                out_str += ':two: '
            elif c == '3':
                out_str += ':three: '
            elif c == '4':
                out_str += ':four: '
            elif c == '5':
                out_str += ':five: '
            elif c == '6':
                out_str += ':six: '
            elif c == '7':
                out_str += ':seven: '
            elif c == '8':
                out_str += ':eight: '
            elif c == '9':
                out_str += ':nine: '
            elif c == '0':
                out_str += ':zero: '

    print(out_str)
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(out_str)
    r.destroy()


def main():
    str = 'a'
    str = input('Enter your text to be memed: \n')
    convert(str)
    input("Press enter to exit...")

main()
