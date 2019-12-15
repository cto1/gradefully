import sqlite3
from sqlite3 import Error
 
 
def create_connection():
    """ create a database connection to the SQLite database
        specified by the db_file
    :return: Connection object or None
    """
    
    db_file = r"./database/gradefully.db"

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn
 
 
def select_all_users(conn):
    """
    Query all rows in the user table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM user")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 

def login_user(conn, userName, password):
    """
    Query the user table
    :param conn: the Connection object
    :param userName: user entered identifier 
    :param password: user entered password
    :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE email = ? AND password = ?", (userName, password) )

    row = cur.fetchone()

    if row:
        print('You are logged in')
        auth = True 
    else:
        print('Username and password not found')
        auth = False

 
# def select_task_by_priority(conn, priority):
#     """
#     Query tasks by priority
#     :param conn: the Connection object
#     :param priority:
#     :return:
#     """
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
 
#     rows = cur.fetchall()
 
#     for row in rows:
#         print(row)
 
 
def main():
 
    # create a database connection
    conn = create_connection()
    with conn:
        print("1. Query users:")
        select_all_users(conn)
 
        # print("2. Query all tasks")
        # select_all_tasks(conn)
 
 
if __name__ == '__main__':
    
    # global variable for authorisation state of the user 
    auth = False
    main()