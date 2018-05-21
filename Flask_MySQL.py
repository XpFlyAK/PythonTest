from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

connector = mysql.connector.connect(host='localhost', port=3306,
                                    user="root", password='3218769',
                                    database='ibm', charset='utf8')

cursor = connector.cursor()
cursor.execute(
    'CREATE TABLE IF NOT EXISTS flaskSQL2 (id INTEGER PRIMARY KEY AUTO_INCREMENT, name VARCHAR (20),password VARCHAR (10))')
cursor.close()


# cursor.execute('insert into flaskSQL (id,name) VALUES (%s,%s)', ['1', 'Michael'])
# print('cursor.rowcount == ' + str(cursor.rowcount))
# conn.commit()
# cursor.close()
# cursor = conn.cursor()
# cursor.execute('select * from flaskSQL WHERE id=%s', ('1',))
#
# print('cursor.fetchall()==' + str(cursor.fetchall()))
# cursor.close()
# conn.close()


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('home.html')


@app.route('/register', methods=['GET'])
def register_get():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register_post():
    user_name = request.form['user_name']
    user_password = request.form['user_password']
    print(user_name + '===' + user_password)
    if user_name != '' and user_password != '':
        cursor2 = connector.cursor()
        cursor2.execute('insert into flaskSQL2 (name,password) VALUES (%s,%s)',
                        ['123', '44444'])
        print('cursor.rowcount==' + str(cursor.rowcount))
        cursor2.close()
        return render_template('register_ok.html')
    return render_template('register_failed.html')


if __name__ == '__main__':
    app.run(debug=True)
