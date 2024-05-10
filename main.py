from gui import *

def main() :

    window = Tk()
    window.title('Bank of Gotham')
    window.geometry('400x700')
    window.resizable(False, False)
    GUI(window)

    window.mainloop()

if __name__ == "__main__":

    main()