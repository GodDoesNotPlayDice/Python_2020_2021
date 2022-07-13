import functions
def main():
    print('Welcome to junked adder python...')
    while True:
        try:
            lines = functions.lines()
            functions.JunkLinesGen(lines)
        except KeyboardInterrupt:
            print('ok, exit')
            quit()
main()
