import requests, sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn

if __name__ == '__main__':
    db_name = "database.db"
    sql_create_table = """ CREATE TABLE IF NOT EXISTS CLIENT (id integer, key text NOT NULL, date text, decrypted text); """
    conn = create_connection(db_name)

    if conn is not None:
        print("SUCCESS => conection stablished")
    else:
        print("FAILED => Some problems in the db connection")