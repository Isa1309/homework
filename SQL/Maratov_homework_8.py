import sqlite3

database_1 = sqlite3.connect("server.sqlite3")
sql = database_1.cursor()


sql.execute(
    """CREATE TABLE IF NOT EXISTS notes (
    times TEXT,
    affairs TEXT,
    status TEXT
    )
    """
)
database_1.commit()


def to_do_list():
    global notes_times, notes_affairs, notes_status
    notes_times = input('Notes time: ')
    notes_affairs = input('Notes affairs: ')
    notes_status = input('Notes status (completed / not done): ')
    sql.execute(f"SELECT times FROM notes WHERE times = '{notes_times}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO notes VALUES (?, ?, ?)", (notes_times, notes_affairs, notes_status))
        database_1.commit()
        print('Case saved, have a nice day! ')
        for value in sql.execute("SELECT * FROM notes"):
            print(value)
    else:
        if notes_status == 'not done':
            sql.execute(f"UPDATE notes SET status = 'You still haven-t done it!' WHERE times = '{notes_times}'")
            print("You still haven't done it!")
            database_1.commit()
            for value in sql.execute("SELECT * FROM notes"):
                print(value)
        else:
            sql.execute(f"DELETE FROM notes WHERE times = '{notes_times}'")
            database_1.commit()
            print("You have completed this task!\n"
                  "Note deleted")
            for value in sql.execute("SELECT * FROM notes"):
                print(value)


if __name__ == "__main__":
    to_do_list()
# Домашнее задание 8 урок