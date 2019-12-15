import db
import login 
import menu

def main():
    menu.welcome()
    validSelect = menu.welcome().selector()


    while False:
        print(validSelect)
        selected = input()
        print(selected)

if __name__ == '__main__':
    main()