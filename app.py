from flask import Flask, url_for, request, redirect
import datetime
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    return '''
<!doctype html>
<html>
    <head>
        <title>404 - Страница не найдена</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <style>
            body {
                text-align: center;
                padding: 50px;
                font-family: Arial, sans-serif;
            }
            h1 {
                font-size: 80px;
                color: #ff6b6b;
                margin: 0;
            }
            h2 {
                color: #333;
                margin: 20px 0;
            }
            img {
                max-width: 300px;
                margin: 20px auto;
                border-radius: 10px;
            }
            p {
                color: #666;
                max-width: 500px;
                margin: 0 auto 20px;
            }
            a {
                color: #667eea;
                text-decoration: none;
                font-weight: bold;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <h1>404</h1>
        <h2>Страница не найдена</h2>
        
        <img src="''' + url_for('static', filename='404.jpg') + '''" alt="Страница не найдена">
        
        <p>Запрашиваемая страница не существует или была перемещена.</p>
        <p>Проверьте правильность адреса или вернитесь на главную страницу.</p>
        
        <a href="/">← Вернуться на главную</a>
    </body>
</html>''', 404
@app.route("/bad_request")
def bad_request():
    return '''
<!doctype html>
<html>
    <head>
        <title>400 Bad Request</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>400 Bad Request</h1>
        <p>Сервер не может обработать запрос из-за некорректного синтаксиса.</p>
        <a href="/">На главную</a>
    </body>
</html>''', 400

@app.route("/unauthorized")
def unauthorized():
    return '''
<!doctype html>
<html>
    <head>
        <title>401 Unauthorized</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>401 Unauthorized</h1>
        <p>Требуется аутентификация для доступа к ресурсу.</p>
        <a href="/">На главную</a>
    </body>
</html>''', 401

@app.route("/payment_required")
def payment_required():
    return '''
<!doctype html>
<html>
    <head>
        <title>402 Payment Required</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>402 Payment Required</h1>
        <p>Зарезервировано для будущего использования. Первоначально предназначалось для цифровых платежных систем.</p>
        <a href="/">На главную</a>
    </body>
</html>''', 402

@app.route("/forbidden")
def forbidden():
    return '''
<!doctype html>
<html>
    <head>
        <title>403 Forbidden</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>403 Forbidden</h1>
        <p>Доступ к запрошенному ресурсу запрещен.</p>
        <a href="/">На главную</a>
    </body>
</html>''', 403

@app.route("/method_not_allowed")
def method_not_allowed():
    return '''
<!doctype html>
<html>
    <head>
        <title>405 Method Not Allowed</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>405 Method Not Allowed</h1>
        <p>Метод запроса не поддерживается для данного ресурса.</p>
        <a href="/">На главную</a>
    </body>
</html>''', 405

@app.route("/teapot")
def teapot():
    return '''
<!doctype html>
<html>
    <head>
        <title>418 I'm a teapot</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>418 I'm a teapot</h1>
        <p>Я - чайник. Не могу заварить кофе.</p>
        <a href="/">На главную</a>
    </body>
</html>''', 418

@app.errorhandler(500)
def internal_server_error(err):
    return '''
<!doctype html>
<html>
    <head>
        <title>500 - Ошибка сервера</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <style>
            body {
                text-align: center;
                padding: 50px;
                font-family: Arial, sans-serif;
                background-color: #fff5f5;
            }
            h1 {
                font-size: 80px;
                color: #e53e3e;
                margin: 0;
            }
            h2 {
                color: #333;
                margin: 20px 0;
            }
            .error-box {
                background: white;
                padding: 20px;
                border-radius: 10px;
                max-width: 600px;
                margin: 20px auto;
                border-left: 4px solid #e53e3e;
            }
            a {
                display: inline-block;
                padding: 10px 20px;
                background: grey;
                color: black;
                text-decoration: none;
                border-radius: 5px;
                margin: 10px;
            }
            a:hover {
                background: black;
            }
        </style>
    </head>
    <body>
        <h1>500</h1>
        <h2>Внутренняя ошибка сервера</h2>
        
        <div class="error-box">
            <p>На сервере произошла непредвиденная ошибка.</p>
            <p>Мы уже знаем о проблеме и работаем над её решением.</p>
            <p>Попробуйте обновить страницу через несколько минут.</p>
        </div>
        
        <div>
            <a href="/">На главную</a>
            <a href="javascript:location.reload()">Обновить страницу</a>
        </div>
        
        <p style="margin-top: 30px; color: #666; font-size: 14px;">
            Если ошибка повторяется, свяжитесь с администратором: 
            <a href="malito:rita.berezhnayaaa@gmail.com" style="color: #555;">rita.berezhnayaaa@gmail.com</a>
        </p>
    </body>
</html>''', 500

@app.route("/server_error")
def cause_server_error():
    result = 1 / 0
    return "Эта строка никогда не будет выполнена"
@app.route("/")
@app.route("/index")
def index():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
        </header>
        
        <main>
            <nav>
                <ul>
                     <li><a href="/lab1">Первая лабораторная</a></li>
                </ul>
             </nav>
        </main>
        
        <footer>
            <hr>
            &copy; Бережная Маргарита Валерьевна, ФБИ-33, 3 курс, 2025
        </footer>
    </body>
</html>'''    

@app.route("/lab1")
def lab1():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Лабораторная 1</title>
    </head>
    <body>
    <h1>Лабораторная работа 1</h1>
        <p>Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</p>
        
        <a href="/">На главную</a>
        <ul>
            <li><a href="/lab1/author">Автор</a></li>
            <li><a href="/lab1/web">WEB</a></li>
            <li><a href="/lab1/image">Дуб</a></li>
            <li><a href="/lab1/counter">Счетчик</a></li>
            <li><a href="/http_codes">Коды ответов HTTP</a></li>
        </ul>
    </body>
</html>''' 

@app.route("/http_codes")
def http_codes():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Коды ответов HTTP</title>
    </head>
    <body>
        <h1>Коды ответов HTTP</h1>
        <ul>
            <li><a href="/bad_request">400 - Bad Request</a></li>
            <li><a href="/unauthorized">401 - Unauthorized</a></li>
            <li><a href="/payment_required">402 - Payment Required</a></li>
            <li><a href="/forbidden">403 - Forbidden</a></li>
            <li><a href="/method_not_allowed">405 - Method Not Allowed</a></li>
            <li><a href="/teapot">418 - I'm a teapot</a></li>
            <li><a href="/server_error">500 - Internal Server Error</a></li>
        </ul>
        <a href="/">На главную</a>
    </body>
</html>'''

@app.route("/lab1/web")  
def web():
    css_url = url_for('static', filename='lab1.css')
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="{css_url}">
    </head>
    <body>
        <h1>web-сервер на flask</h1>
        <a href="/lab1/author">author</a>
        <br>
        <a href="/lab1">Назад к главной</a>
    </body>
</html>'''

@app.route("/lab1/author")  
def author():
    name = "Бережная Маргарита Валерьевна"
    group = "ФБИ-33"
    faculty = "ФБ"
    css_url = url_for('static', filename='lab1.css')
    
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="{css_url}">
    </head>           
    <body>
        <p>Студент: {name}</p>
        <p>Группа: {group}</p>
        <p>Факультет: {faculty}</p>
        <a href="/lab1/web">web</a>
        <br>
        <a href="/lab1">Назад к главной</a>
    </body>
</html>''', 200, {
        'Content-Language': 'ru-RU',  
        'X-Image-Type': 'Nature',     
        'X-Server-Location': 'Novosibirsk',  
        'X-Student-Name': 'Berezhnaya Margarita' 
    }

@app.route('/lab1/image')  
def image():
    path = url_for("static", filename="oak.jpg")
    css_url = url_for('static', filename='lab1.css')  
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="{css_url}">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="{path}">
        <br>
        <a href="/lab1">Назад к главной</a>
    </body>
</html>
'''

count = 0

@app.route('/lab1/counter') 
def counter():
    global count
    count += 1
    time = datetime.datetime.today()  
    url = request.url
    client_ip = request.remote_addr
    css_url = url_for('static', filename='lab1.css')  
    
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="{css_url}">
    </head>
    <body>
        <h2>Счетчик посещений</h2>
        Сколько раз вы сюда заходили: {count}
        <hr>
        Дата и время: {time}<br>
        Запрошенный адрес: {url}<br>
        Ваш IP-адрес: {client_ip}<br>
        <a href="/lab1">Назад к главной</a>
        <br>
        <a href="/reset_counter">Очистить счётчик</a>
    </body>
</html>
'''

@app.route('/reset_counter')
def reset_counter():
    global count
    count = 0
    return redirect('/lab1/counter') 

@app.route("/lab1/info")
def info():    
    return redirect("/lab1/author") 

@app.route("/created")
def created():
    css_url = url_for('static', filename='lab1.css')
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="{css_url}">
    </head>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
        <a href="/lab1">Назад к главной</a>
    </body>
</html>
''', 201

if __name__ == '__main__':
    app.run(debug=True)