from flask import Blueprint, render_template, request, redirect, session
lab5 = Blueprint('lab5', __name__)
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash

def init_db():
    """Инициализация базы данных с созданием таблиц и прав"""
    try:
        conn = psycopg2.connect(
            host='127.0.0.1',
            database='margarita_berezhnaya_knowledge_base',  
            user='postgres',  
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

        cur.execute('GRANT ALL PRIVILEGES ON TABLE users TO margarita_berezhnaya_knowledge_base')
        cur.execute('GRANT ALL PRIVILEGES ON SEQUENCE users_id_seq TO margarita_berezhnaya_knowledge_base')
        
        conn.commit()
        cur.close()
        conn.close()
        print(" Таблица users создана и права выданы")
 
        return check_user_access()
        
    except Exception as e:
        print(f" Ошибка при инициализации БД: {e}")
        return False

def check_user_access():
    """Проверка доступа обычного пользователя к таблице"""
    try:
        conn = psycopg2.connect(
            host='127.0.0.1',
            database='margarita_berezhnaya_knowledge_base',  
            user='margarita_berezhnaya_knowledge_base',      
            password='123',
            port=5432
        )
        cur = conn.cursor()

        cur.execute("SELECT 1 FROM users LIMIT 1")
        result = cur.fetchone()
        
        cur.close()
        conn.close()
        print(" Доступ к таблице users подтвержден")
        return True
        
    except Exception as e:
        print(f" Нет доступа к таблице users: {e}")
        return False

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
        print(f"Таблицы в базе: {tables}")

        try:
            cur.execute("SELECT COUNT(*) FROM users")
            count = cur.fetchone()[0]
            print(f" Количество пользователей в БД: {count}")
        except psycopg2.Error as e:
            print(f"  Нет доступа к таблице users: {e}")
        
        cur.close()
        conn.close()
        return True
    except Exception as e:
        print(f" Ошибка подключения: {e}")
        return False

print("🔍 Проверяем подключение к БД...")
check_connection()

if not init_db():
    print("  Проблема с инициализацией БД, но продолжаем работу")

@lab5.route('/lab5/')
def lab():
    return render_template('lab5/lab5.html', username=session.get('login', 'anonymous'))

def db_connect():
    try:
        conn = psycopg2.connect(
            host='127.0.0.1',
            database='margarita_berezhnaya_knowledge_base',  
            user='margarita_berezhnaya_knowledge_base',      
            password='123',
            port=5432
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
        return conn, cur
    except Exception as e:
        print(f" Ошибка подключения к БД: {e}")
        raise

def db_close(conn, cur):
    try:
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"  Ошибка при закрытии соединения: {e}")

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
            db_close(conn, cur)
            return render_template('lab5/register.html',
                                error="Такой пользователь уже существует")

        print(f"➕ Добавляем пользователя: {login}")
        password_hash = generate_password_hash(password)
        cur.execute("INSERT INTO users (login, password) VALUES (%s, %s)", (login, password_hash))
        conn.commit()

        print(f"Пользователь {login} добавлен в БД")
        
        db_close(conn, cur)
        
        return render_template('lab5/success.html', login=login)
    
    except psycopg2.Error as e:
        print(f" Ошибка PostgreSQL: {e}")
        error_msg = "Ошибка доступа к базе данных. Таблица не доступна для записи."
        return render_template('lab5/register.html', error=error_msg)
    except Exception as e:
        print(f" Общая ошибка: {e}")
        return render_template('lab5/register.html', error=f'Ошибка: {str(e)}')
    

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
        
        cur.execute("SELECT * FROM users WHERE login = %s", (login,))
        user = cur.fetchone()
        
        if user and check_password_hash(user['password'], password):
            session['login'] = login
            session['user_id'] = user['id']
            db_close(conn, cur)
            return redirect('/lab5/')
        else:
            db_close(conn, cur)
            return render_template('lab5/login.html', error="Неверный логин или пароль")
    
    except psycopg2.Error as e:
        print(f" Ошибка PostgreSQL при входе: {e}")
        return render_template('lab5/login.html', error="Ошибка доступа к базе данных")
    except Exception as e:
        print(f" Общая ошибка при входе: {e}")
        return render_template('lab5/login.html', error=f'Ошибка: {str(e)}')


@lab5.route('/lab5/logout')
def logout():
    session.clear()
    return redirect('/lab5/')