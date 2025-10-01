from flask import Flask, url_for, request, redirect
import datetime
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    return "Нет такой страницы", 404

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
            <li><a href="/lab1/author">author</a></li>
            <li><a href="/lab1/web">web</a></li>
            <li><a href="/lab1/image">image</a></li>
            <li><a href="/lab1/counter">counter</a></li>
        </ul>
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
</html>'''
    

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