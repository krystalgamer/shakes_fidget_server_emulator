import sqlite3

conn = None
cursor = None


def StartDb(name='db.sql'):
    global conn, cursor
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    return


def QueryDb(query, args, fetchall=False):
    global conn, cursor
    qr = cursor.execute(query, args)
    if fetchall:
        qr = qr.fetchall()

    return qr


def CloseDb():
    global conn, cursor
    cursor.close()
    conn.close()
