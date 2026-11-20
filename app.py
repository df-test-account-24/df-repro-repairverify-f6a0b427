from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)
@app.route("/search")
def search():
    q = request.args.get("q", "")
    connection = sqlite3.connect("test_records.db")
    connection.execute("CREATE TABLE IF NOT EXISTS test_records (name TEXT)")
    rows = connection.execute("SELECT name FROM test_records WHERE name = '" + q + "'").fetchall()
    connection.close()
    return jsonify([row[0] for row in rows])
