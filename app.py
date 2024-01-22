from flask import Flask, render_template
import pymysql  # 모듈 import

app = Flask(__name__)

# Mysql 데이터베이스 연결
db = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="class-password",
    db="kream",
    charset="utf8mb4",
)

# 데이터 접근
cur = db.cursor()
sql = "SELECT * FROM kream"  # SQL query 작성
cur.execute(sql)  # sql 실행

kream_data = cur.fetchall()  # db 데이터 모든 행 가져오기


@app.route("/")
def index():
    return render_template("index.html", data_list=kream_data)


if __name__ == "__main__":
    app.run(debug=True)
