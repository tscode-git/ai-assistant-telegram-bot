import sqlite3

db=sqlite3.connect("ai_bot.db")
c=db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, model TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS messages(id INTEGER PRIMARY KEY,user_id INTEGER,role TEXT,text TEXT)')
db.commit()

def add_user(uid):
    c.execute("INSERT OR IGNORE INTO users VALUES(?,?)",(uid,"google/gemini-2.0-flash-exp:free"))
    db.commit()

def set_model(uid, model):
    c.execute("UPDATE users SET model=? WHERE id=?",(model,uid))
    db.commit()

def get_model(uid):
    r=c.execute("SELECT model FROM users WHERE id=?",(uid,)).fetchone()
    return r[0] if r else "google/gemini-2.0-flash-exp:free"

def clear(uid):
    c.execute("DELETE FROM messages WHERE user_id=?",(uid,))
    db.commit()

def save(uid,role,text):
    c.execute("INSERT INTO messages(user_id,role,text) VALUES(?,?,?)",(uid,role,text))
    db.commit()

def history(uid):
    return c.execute("SELECT role,text FROM messages WHERE user_id=? ORDER BY id",(uid,)).fetchall()

def count_messages(uid):
    return c.execute("SELECT COUNT(*) FROM messages WHERE user_id=?",(uid,)).fetchone()[0]
