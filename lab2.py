from flask import Blueprint, url_for, request, redirect, render_template, abort

lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/a')
def a():
    return 'без слэша'

@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = [
    {'name': 'роза', 'price': 300},
    {'name': 'тюльпан', 'price': 310},
    {'name': 'незабудка', 'price': 320},
    {'name': 'ромашка', 'price': 330},
    {'name': 'георгин', 'price': 300},
    {'name': 'гладиолус', 'price': 310}
]

@lab2.route('/lab2/flowers/')
def flowers_list():
    return render_template('flowers.html', flowers=flower_list)

@lab2.route('/lab2/del_flower/<int:flower_id>')
def del_flower(flower_id):
    if flower_id >= len(flower_list):
        abort(404)
    flower_list.pop(flower_id)
    return redirect(url_for('lab2.flowers_list'))

@lab2.route('/lab2/add_flower/', methods=['GET', 'POST'])
def add_flower():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        if name:
            for flower in flower_list:
                if flower['name'] == name:
                    flower['price'] += 10
                    break
            else:
                flower_list.append({'name': name, 'price': 300})
        return redirect(url_for('lab2.flowers_list'))
    return redirect(url_for('lab2.flowers_list'))
    
@lab2.route('/lab2/flowers/all')
def all_flowers():
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Все цветы</h1>
        <p>Количество цветов: {len(flower_list)}</p>
        <p>Полный список: {flower_list}</p>
        <a href="/lab2/flowers/clear">Очистить список</a>
    </body>
</html>
'''

@lab2.route('/lab2/flowers/clear')
def clear_flowers():
    flower_list.clear()
    return redirect(url_for('lab2.flowers_list'))

@lab2.route('/lab2/example')
def example():
    name = "Бережная Маргарита Валерьевна"
    number = "33"
    group = "ФБИ-33"
    course = "3 курс"
    
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321},
    ]
    return render_template('example.html', 
                           name=name, number=number, group=group, 
                           course=course, fruits=fruits)

@lab2.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase=phrase)

@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return f'''
<!doctype html>
<html>
<body>
    <h1>Расчёт с параметрами:</h1>
    <div class="result">
        {a} + {b} = {a + b}<br>
        {a} - {b} = {a - b}<br>
        {a} × {b} = {a * b}<br>
        {a} / {b} = {a / b if b != 0 else 'на ноль делить нельзя'}<br>
        {a}<sup>{b}</sup> = {a ** b}
    </div>
    <p><a href="/lab2/calc/">Попробовать с другими числами</a></p>
</body>
</html>
'''

@lab2.route('/lab2/calc/')
def calc_default():
    return redirect('/lab2/calc/1/1')

@lab2.route('/lab2/calc/<int:a>')
def calc_single(a):
    return redirect(f'/lab2/calc/{a}/1')

books = [
    {'author': 'Фёдор Достоевский', 'title': 'Преступление и наказание', 'genre': 'Роман', 'pages': 671},
    {'author': 'Джордж Оруэлл', 'title': '1984', 'genre': 'Антиутопия', 'pages': 320},
    {'author': 'Джоан Роулинг', 'title': 'Гарри Поттер и философский камень', 'genre': 'Фэнтези', 'pages': 400},
    {'author': 'Агата Кристи', 'title': 'Убийство в Восточном экспрессе', 'genre': 'Детектив', 'pages': 250},
    {'author': 'Александр Пушкин', 'title': 'Евгений Онегин', 'genre': 'Роман в стихах', 'pages': 240},
    {'author': 'Эрих Мария Ремарк', 'title': 'Три товарища', 'genre': 'Военная проза', 'pages': 380},
    {'author': 'Александр Дюма', 'title': 'Граф Монте-Кристо', 'genre': 'Исторический приключенческий роман', 'pages': 1200},
    {'author': 'Джон Р. Р. Толкин', 'title': 'Властелин Колец', 'genre': 'Эпическое фэнтези', 'pages': 1100},
    {'author': 'Эрнест Хемингуэй', 'title': 'Старик и море', 'genre': 'Притча', 'pages': 110},
    {'author': 'Михаил Лермонтов', 'title': 'Герой нашего времени', 'genre': 'Роман', 'pages': 224},
]

@lab2.route('/lab2/books/')
def books_list():
    return render_template('books.html', books=books)

@lab2.route('/lab2/cars/')
def cars():
    cars_list = [
        {
            'name': 'Ford Mustang',
            'year': '1964',
            'description': 'Легендарный американский маслкар, символ свободы и скорости.',
            'image': 'ford_mustang.jpg',
            'country': 'США',
            'type': 'Спортивный автомобиль'
        },
        {
            'name': 'Volkswagen Beetle',
            'year': '1938',
            'description': 'Народный автомобиль, один из самых узнаваемых в мире.',
            'image': 'vw_beetle.jpg',
            'country': 'Германия',
            'type': 'Компактный автомобиль'
        },
        {
            'name': 'Toyota Corolla',
            'year': '1966',
            'description': 'Самый продаваемый автомобиль в истории - надежность и практичность.',
            'image': 'toyota_corolla.jpg',
            'country': 'Япония',
            'type': 'Седан'
        },
        {
            'name': 'Ferrari F40',
            'year': '1987',
            'description': 'Легендарный суперкар, последний автомобиль, одобренный Энцо Феррари.',
            'image': 'ferrari_f40.jpg',
            'country': 'Италия',
            'type': 'Суперкар'
        },
        {
            'name': 'Jeep Wrangler',
            'year': '1986',
            'description': 'Внедорожник с культовым дизайном, наследник военного Willys MB.',
            'image': 'jeep_wrangler.jpg',
            'country': 'США',
            'type': 'Внедорожник'
        },
        {
            'name': 'BMW 3 Series',
            'year': '1975',
            'description': 'Икона спортивных седанов, сочетание комфорта и динамики.',
            'image': 'bmw_3series.jpg',
            'country': 'Германия',
            'type': 'Спортивный седан'
        },
        {
            'name': 'Lada Niva',
            'year': '1977',
            'description': 'Первый в мире моноприводный внедорожник, легенда российского автопрома.',
            'image': 'lada_niva.jpg',
            'country': 'Россия',
            'type': 'Внедорожник'
        },
        {
            'name': 'Porsche 911',
            'year': '1963',
            'description': 'Культовый спортивный автомобиль с задним расположением двигателя.',
            'image': 'porsche_911.jpg',
            'country': 'Германия',
            'type': 'Спортивный автомобиль'
        },
        {
            'name': 'Honda Civic',
            'year': '1972',
            'description': 'Компактный автомобиль, ставший иконой тюнинговой культуры.',
            'image': 'honda_civic.jpg',
            'country': 'Япония',
            'type': 'Компактный автомобиль'
        },
        {
            'name': 'Mercedes-Benz S-Class',
            'year': '1972',
            'description': 'Флагманский седан, эталон роскоши и технологий.',
            'image': 'mercedes_sclass.jpg',
            'country': 'Германия',
            'type': 'Представительский класс'
        },
        {
            'name': 'Chevrolet Corvette',
            'year': '1953',
            'description': 'Американский спортивный автомобиль, символ автоиндустрии США.',
            'image': 'chevrolet_corvette.jpg',
            'country': 'США',
            'type': 'Спортивный автомобиль'
        },
        {
            'name': 'Volvo XC90',
            'year': '2002',
            'description': 'Премиальный внедорожник, известный своей безопасностью.',
            'image': 'volvo_xc90.jpg',
            'country': 'Швеция',
            'type': 'Внедорожник'
        },
        {
            'name': 'Mazda MX-5 Miata',
            'year': '1989',
            'description': 'Легкий родстер, возродивший класс доступных спортивных автомобилей.',
            'image': 'mazda_mx5.jpg',
            'country': 'Япония',
            'type': 'Родстер'
        },
        {
            'name': 'Range Rover',
            'year': '1970',
            'description': 'Роскошный внедорожник, создавший новый класс автомобилей.',
            'image': 'range_rover.jpg',
            'country': 'Великобритания',
            'type': 'Премиальный внедорожник'
        },
        {
            'name': 'Tesla Model S',
            'year': '2012',
            'description': 'Электрический седан, изменивший представление об электромобилях.',
            'image': 'tesla_models.jpg',
            'country': 'США',
            'type': 'Электромобиль'
        },
        {
            'name': 'Audi Quattro',
            'year': '1980',
            'description': 'Легенда ралли, популяризировавший полный привод в гражданских авто.',
            'image': 'audi_quattro.jpg',
            'country': 'Германия',
            'type': 'Спортивный автомобиль'
        },
        {
            'name': 'Nissan GT-R',
            'year': '2007',
            'description': 'Японский суперкар, известный как "Богzilla" за свою производительность.',
            'image': 'nissan_gtr.jpg',
            'country': 'Япония',
            'type': 'Суперкар'
        },
        {
            'name': 'Fiat 500',
            'year': '1957',
            'description': 'Культовый городской автомобиль, символ итальянского стиля.',
            'image': 'fiat_500.jpg',
            'country': 'Италия',
            'type': 'Городской автомобиль'
        },
        {
            'name': 'Lamborghini Countach',
            'year': '1974',
            'description': 'Суперкар с клиновидным дизайном, икона 1980-х годов.',
            'image': 'lamborghini_countach.jpg',
            'country': 'Италия',
            'type': 'Суперкар'
        },
        {
            'name': 'Subaru Impreza WRX',
            'year': '1992',
            'description': 'Легенда раллийных соревнований с оппозитным двигателем и полным приводом.',
            'image': 'subaru_impreza.jpg',
            'country': 'Япония',
            'type': 'Спортивный седан'
        }
    ]
    
    return f'''
<!doctype html>
<html>
    <head>
        <title>Коллекция автомобилей</title>
    </head>
    <body>
        <h1>Коллекция легендарных автомобилей</h1>
        <a href="/">На главную</a>
        <div class="cars-container">
            {''.join([f'''
            <div class="car-card">
                <h2>{car["name"]}</h2>
                <img src="{url_for('static', filename=car['image'])}" alt="{car['name']}" width="300">
                <div class="car-info">
                    <p><strong>Год выпуска:</strong> {car["year"]}</p>
                    <p><strong>Страна:</strong> {car["country"]}</p>
                    <p><strong>Тип:</strong> {car["type"]}</p>
                    <p><strong>Описание:</strong> {car["description"]}</p>
                </div>
            </div>
            ''' for car in cars_list])}
        </div>
    </body>
</html>
'''