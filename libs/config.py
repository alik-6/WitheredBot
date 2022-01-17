import sqlite3

DATABASE_NAME = "Storage.db"
def database():
    connection = sqlite3.connect(DATABASE_NAME)
    conn = connection.cursor()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS Settings (
        key TEXT NOT NULL UNIQUE,
        value TEXT
    );
    """)
    connection.commit()
    connection.close()

def get(key: str):
    database()
    connection = sqlite3.connect(DATABASE_NAME)
    conn = connection.cursor()
    value = conn.execute("SELECT * FROM Settings where key = ?;", (key,)).fetchone()
    connection.commit()
    connection.close()
    if value:
        return value[1]
    else:
        return None



def set(key:str, value: str):
    database()
    connection = sqlite3.connect(DATABASE_NAME)
    conn = connection.cursor()
    try:
        conn.execute("INSERT INTO Settings(key, value) VALUES(? , ?);", (key, value,))
        connection.commit()
        connection.close()
        return {'Added': 'Key Added'}
    except sqlite3.IntegrityError:
        return {'Error': 'Key Already Exist'}

def delete(key: str):
    database()
    connection = sqlite3.connect(DATABASE_NAME)
    conn = connection.cursor()
    conn.execute("DELETE FROM Settings WHERE key = ?",(key,))
    connection.commit()
    connection.close()

def update(key:str, value: str):
    database()
    connection = sqlite3.connect(DATABASE_NAME)
    conn = connection.cursor()
    value = conn.execute(f"UPDATE Settings SET value = '{value}' WHERE key = '{key}'")
    connection.commit()
    connection.close()




