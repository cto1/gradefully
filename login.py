import db

def main():
    userName = ''
    password = ''

    # capture username 
    while userName == '':
        userName = input('Enter your username:')

    # capture password
    while password == '':
        password = input('Enter your password:')

    # create a database connection
    conn = db.create_connection()
    with conn:
        print('Trying to login... with ' + userName +  password)
        db.login_user(conn, userName, password)

if __name__ == '__main__':
    main()