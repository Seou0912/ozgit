<img width="1085" alt="Screenshot 2024-01-22 at 11 26 25" src="https://github.com/Seou0912/ozgit/assets/151927766/4b01b75d-51b5-4ac7-aa70-96bf1c5ae999">
  
무슨 문제로 안되었었는지 처음부터 확인하며 작성해본다.  
정말 스팀이 점점 올라왔다.  
왜 ~~  
왜!!  
왜???  
왜? 뭣 때문에!!!  
왜땜에???  
안되는 거야?  
뭐가 문제인거냐구!!!  

# 1.Kream 사이트에서 브랜드 설정하여 카테고리별로 데이터를 가져와 DB에 넣는다.  

<img width="1024" alt="Screenshot 2024-01-22 at 11 13 47" src="https://github.com/Seou0912/ozgit/assets/151927766/9a990c04-bd9a-409f-8414-0a0ec1efedf0">

>> 데이터는 잘 들어와있다.  
# 2. pymysql 이용 테이블에 넣기    
import pymysql  

connection = pymysql.connect(  
host="127.0.0.1",  
생략....  
  
# 3. Flask ->Bootstrap 적용하기   
가상환경 설치 >sudo pip3 install virtualenv  
clawing 이름으로 virtualenv 가상환경 만들기 virtualenv clawing -> mkdir clawing -> cd clawing  
가상환경 활성화 하기 clawing>source bin/activate  
이후 Flask 설치 clawing>pip3 install Flask  
app.py 생성  
from flask import Flask  
<br/>
app = Flask(__name__)  
<br/> 
@app.route('/')   
def index():  
return 'Hello, Flask!'  

if __name__ == '__main__':  
app.run(debug=True)  

- app.py 실행 기본화일로 성정하고 실행  
**export FLASK_APP=app.py**  
clawing>flask run #정상 작동하면 접속 가능한 주소 보여줌  
**http://127.0.0.1:5000** // 종료 ^c  
>> 잘 실행 됨
<img width="729" alt="Screenshot 2024-01-18 at 14 20 17" src="https://github.com/Seou0912/ozgit/assets/151927766/f286bc3a-46a8-4cca-92f9-a14f819c4c0f">
  
# 4. bootstrap 적용  
https://getbootstrap.kr/ Down css,js  
clawing/static 생성  
그안에 css, js copy  

<br/>  
# 5. admin page -> clawing/template 폴더 생성 후 가져옴   
   
링크코드 변경   
**<link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.min.css') }}">**
**<script src="{{ url_for('static', filename='bootstrap.min.js') }}"></script>**
![Screenshot 2024-01-14 at 18 34 40](https://github.com/Seou0912/ozgit/assets/151927766/c4a343a7-3cee-45d6-a195-e1c699c274e4)

>> 잘 실행 되고 있다.  
<br/>
# 6. flask에 scraping result database linking      
appy.py   
from flask import Flask, render_template   
import pymysql // 모듈 import   
<br/>  
 // Mysql 데이터베이스 연결**   
db = pymysql.connect(   
host="127.0.0.1",  
user="root",  
password="class-password",  
db="kream",  
charset="utf8mb4",  
cursorclass=pymysql.cursors.DictCursor,  
)  
  
app = Flask(__name__)  
  
**// 데이터 접근**   
cur = db.cursor()   
sql = "SELECT * FROM kream" # SQL query 작성  
cur.exevute---오타(sql) # sql 실행  
  
kream_data = cur.fetchall() # db 데이터 모든 행 가져오기  

@app.route("/")  
def index():  
return render_template("index.html", data_list=kream_data)  
  
if __name__ == "__main__":  
app.run(debug=True)  
app.run  
  
이제 flask run 하면 실행이 되야하는  
<img width="1324" alt="Screenshot 2024-01-19 at 16 21 39" src="https://github.com/Seou0912/ozgit/assets/151927766/8dd9cdb6-110b-4eb5-a3c6-94f18c7367fa">
데~~~  

![Screenshot 2024-01-19 at 17 53 08](https://github.com/Seou0912/ozgit/assets/151927766/aacc222b-0280-4fbf-8f20-6d20cc8c6df9)


미춰버리겠네......  
뭘까?  
무멀까요?  
왤까요?  
뭘 안한 건 까요?  
코드에서 뭐 오타 있나요?  
  
해결! 1. 오타 ㅋㅋ 역시 오타  
template ->templats "s"  
appy.py 화일안에 exevute -execute  
해결! 2. db 데이터 가져오기  
  
이건 또 뭔일  
varbinary -> str  
varbinary -> int # 이건 했는데 price 왠 일!!  
  
**DB table 생성시 varchar로** 하니 되더라는,,,  
str과 int 변환해서 출력하는 것을 더 해봐야겠다.  
