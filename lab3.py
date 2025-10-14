from flask import Blueprint, render_template, request, make_response, redirect

lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    return render_template('lab3.html', name=name, name_color=name_color)  

@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp

@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp

@lab3.route('/lab3/form1')
def form1():
    user = request.args.get('user')
    age = request.args.get('age')
    sex = request.args.get('sex')
    
    print(f"DEBUG: user={user}, age={age}, sex={sex}")  
    
    errors = {}
  
    if any([user, age, sex]):
        if not user or user.strip() == '':
            errors['user'] = 'Заполните поле!'
        if not age or age.strip() == '':
            errors['age'] = 'Заполните поле!'
        
        print(f"DEBUG: errors={errors}")  

        if errors:
            return render_template('form1.html', 
                                 user=user or '', age=age or '', sex=sex or '', 
                                 errors=errors)
        
        if user and age and sex:
            return render_template('form1.html', 
                                 user=user, age=age, sex=sex)
    
    return render_template('form1.html', user=user or '', age=age or '', sex=sex or '')