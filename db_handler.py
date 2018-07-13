import sqlite3

IntegrityError = sqlite3.IntegrityError

conn = None
cursor = None


def StartDb(name='sf.db'):
    global conn, cursor
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute(' CREATE TABLE IF NOT EXISTS players(id INTEGER PRIMARY_KEY NOT NULL DEFAULT 1 , username TEXT UNIQUE, password TEXT, email TEXT, sex INT, race INT, class INT, face TEXT, unk5 INT, logincount INT, banned TEXT DEFAULT NULL)')
    conn.commit()
    return


def QueryDb(query, args, fetchall=False):
    global conn, cursor

    qr = cursor.execute(query, args)
    if fetchall:
        qr = qr.fetchall()

    conn.commit()
    return qr


def CloseDb():
    global conn, cursor
    cursor.close()
    conn.close()
    return
