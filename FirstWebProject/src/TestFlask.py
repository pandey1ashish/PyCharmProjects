import sqlite3
from flask import Flask, redirect, request, render_template

app = Flask(__name__, static_url_path='')

def sqlConn():
    conn = sqlite3.connect('testDb.db')
    #print('Conn success!')
    cursor = conn.execute("select 121, 'Ashish'")
    #cursor = conn.execute("SELECT name FROM TEST.sqlite_master WHERE type='table' ORDER BY name")
    #"select col_id, col_name from sample_table")
    #print('Query executed....')
    for row in cursor:
        outvar = 'Rec Id => %s And Name => %s'%(row[0],row[1])
        return outvar
    conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sqlfn")
def sqlfn():
    return sqlConn()

if __name__ == "__main__":
    app.run()