from flask import Blueprint, render_template, request, redirect, session
lab5 = Blueprint('lab5', __name__)
import psycopg2
from psycopg2.extras import RealDictCursor

def check_connection():
    """Функция для проверки подключения к БД"""
    try:
        conn = psycopg2.connect(
            host='127.0.0.1',
            database='margarita_berezhnaya_knowledge_base',  
            user='margarita_berezhnaya_knowledge_base',      
            password='123',
            port=5432
        )
        cur = conn.cursor()

        cur.execute("SELECT current_database()")
        current_db = cur.fetchone()[0]
        print(f" Подключены к базе данных: {current_db}")

        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """)
        tables = cur.fetchall()
        print(f" Таблицы в базе: {tables}")

        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        print(f"👥 Пользователи в БД: {users}")
        
        cur.close()
        conn.close()
        return True
    except Exception as e:
        print(f" Ошибка подключения: {e}")
        return False

print("🔍 Проверяем подключение к БД...")
check_connection()

def init_db():
    try:
        conn = psycopg2.connect(
            host='127.0.0.1',
            database='margarita_berezhnaya_knowledge_base',  
            user='margarita_berezhnaya_knowledge_base',      
            password='123',
            port=5432
        )
        cur = conn.cursor()

        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                login VARCHAR(30) UNIQUE NOT NULL,
                password VARCHAR(162) NOT NULL
            )
        ''')
        
        conn.commit()
        cur.close()
        conn.close()
        print(" Таблица users проверена/создана")
    except Exception as e:
        print(f" Ошибка при инициализации БД: {e}")

init_db()

@lab5.route('/lab5/')
def lab():
    return render_template('lab5/lab5.html', username=session.get('login', 'anonymous'))

def db_connect():
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='margarita_berezhnaya_knowledge_base',  
        user='margarita_berezhnaya_knowledge_base',      
        password='123',
        port=5432
    )
    cur = conn.cursor(cursor_factory = RealDictCursor)

    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()  

@lab5.route('/lab5/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login and password):
        return render_template('lab5/register.html', error='Заполните все поля')

    if len(login) < 3:
        return render_template('lab5/register.html', error='Логин должен быть не менее 3 символов')
    
    if len(password) < 3:
        return render_template('lab5/register.html', error='Пароль должен быть не менее 3 символов')
    
    try:
         conn, cur = db_connect()

        print(f" Проверяем пользователя: {login}")
        cur.execute("SELECT login FROM users WHERE login = %s", (login,))
        existing_user = cur.fetchone()
        
        if existing_user:
            print(f" Пользователь уже существует: {existing_user}")
            cur.close()
            conn.close()
            return render_template('lab5/register.html',
                                error="Такой пользователь уже существует")

        print(f" Добавляем пользователя: {login}")
        cur.execute("INSERT INTO users (login, password) VALUES (%s, %s)", (login, password))
        conn.commit()

        cur.execute("SELECT * FROM users WHERE login = %s", (login,))
        new_user = cur.fetchone()
        print(f" Пользователь добавлен: {new_user}")

        cur.execute("SELECT * FROM users")
        all_users = cur.fetchall()
        print(f"📋 Все пользователи в БД: {all_users}")
        
        db_close(conn, cur)
        
        return render_template('lab5/success.html', login=login)
    
    except Exception as e:
        print(f" Ошибка: {e}")
        return render_template('lab5/register.html', error=f'Ошибка базы данных: {str(e)}')
    

@lab5.route('/lab5/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab5/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login and password):
        return render_template('lab5/login.html', error="Заполните поля")
    
    try:
        conn, cur = db_connect()
        
        cur.execute(f"SELECT * FROM users WHERE login='{login}';")
        user = cur.fetchone()

    if not user:
            db_close(conn, cur)
            return render_template('lab5/login.html',
                                error='Логин и/или пароль неверны')
        
    if user['password'] != password:
            db_close(conn, cur)
            return render_template('lab5/login.html',
                                error='Логин и/или пароль неверны')
        
        session['login'] = login
        db_close(conn, cur)
        return render_template('lab5/success_login.html', login=login)
    
    except psycopg2.OperationalError as e:
        return render_template('lab5/login.html', error=f'Ошибка подключения к БД: {str(e)}')
    except Exception as e:
        return render_template('lab5/login.html', error=f'Ошибка базы данных: {str(e)}')