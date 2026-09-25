import sqlite3

with sqlite3.connect(":memory:") as conn:
    cur = conn.cursor()
    # CREATE
    cur.execute("CREATE TABLE users (id INTEGER, name TEXT)")
    # INSERT — несколько строк через executemany
    cur.executemany(
        "INSERT INTO users VALUES (?, ?)",
        [(1, "Dima"), (2, "Egor")]
    )
    # UPDATE
    cur.execute("UPDATE users SET name=? WHERE id=?", ("Oleg", 1))
    # DELETE
    cur.execute("DELETE FROM users WHERE id=?", (2,))

    # SELECT + проверка целостности
    cur.execute("SELECT name FROM users WHERE id=?", (1,))
    assert cur.fetchone()[0] == "Oleg", "Имя не обновилось"
    print("Проверка целостности OK ✅")

    # Обработка исключения
    try:
        cur.execute("INSERT INTO users VALUES (?, ?)", (3, "Oleg"))  # дубликат name
    except sqlite3.IntegrityError as e:
        print("Дубликат:", e)
        conn.rollback()