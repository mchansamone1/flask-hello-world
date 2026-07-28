from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")
conn = None
cur = None

try:
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    # SQL work goes here

    conn.commit()
    return "Success message here"
except Exception as e:
    if conn is not None:
        conn.rollback()
    return f"Database error: {e}"
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


@app.route("/")
def index():
    return "Hello World from Mason Chansamone in 3308"
