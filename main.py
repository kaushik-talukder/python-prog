import sqlite3 as sl
from tinydb import TinyDB, Query


def main():
    con = sl.connect('/Users/kaushik/Workspace/database/relational-database.db')
    with con:
        data = con.execute("SELECT * FROM USERS")
        for row in data:
            print(row)
    db = TinyDB('/Users/kaushik/Workspace/database/non-relational-database.json')
    # db.insert({'name': 'Kaushik', 'age': 35})
    user = Query()
    print(db.search(user.age == 35))


if __name__ == "__main__":
    main()
