from django.shortcuts import render, redirect
from bson import ObjectId
from .models import vehiculos_collection

def require_admin(request):
    if request.session.get('role') != 'admin':
        return redirect('login')
    return None


def require_client(request):
    if request.session.get('role') not in ('cliente', 'admin'):
        return redirect('login')
    return None


def login_view(request):
    if request.session.get('role') == 'admin':
        return redirect('vehiculo-list')
    if request.session.get('role') == 'cliente':
        return redirect('vehiculo-cliente')

    error = None
    username = ''

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if username == 'admin' and password == 'admin123':
            request.session['role'] = 'admin'
            request.session['user'] = 'Administrador'
            return redirect('vehiculo-list')
        elif username == 'cliente' and password == 'cliente123':
            request.session['role'] = 'cliente'
            request.session['user'] = 'Cliente'
            return redirect('vehiculo-cliente')

        error = 'Usuario o contraseña incorrectos.'

    return render(request, 'mongoapp/login.html', {
        'error': error,
        'username': username,
    })


def logout_view(request):
    request.session.flush()
    return redirect('login')


def vehiculo_list(request):
    redirect_response = require_admin(request)
    if redirect_response:
        return redirect_response

    vehiculos = list(vehiculos_collection.find())
    for v in vehiculos:
        v['id'] = str(v['_id'])

    disponibles = sum(1 for v in vehiculos if v.get('status') == 'disponible')
    vendidos = sum(1 for v in vehiculos if v.get('status') == 'vendido')

    return render(request, 'mongoapp/vehiculo_list.html', {
        'vehiculos': vehiculos,
        'disponibles': disponibles,
        'vendidos': vendidos,
        'role': request.session.get('role'),
        'user_name': request.session.get('user'),
    })

def vehiculo_create(request):
    redirect_response = require_admin(request)
    if redirect_response:
        return redirect_response

    if request.method == 'POST':
        vehiculo = {
            'make': request.POST['make'],
            'model': request.POST['model'],
            'price': request.POST['price'],
            'color': request.POST['color'],
            'year': request.POST['year'],
            'status': request.POST['status'],
        }
        vehiculos_collection.insert_one(vehiculo)
        return redirect('vehiculo-list')
    return render(request, 'mongoapp/vehiculo_form.html')

def vehiculo_update(request, pk):
    redirect_response = require_admin(request)
    if redirect_response:
        return redirect_response

    vehiculo = vehiculos_collection.find_one({'_id': ObjectId(pk)})
    vehiculo['id'] = str(vehiculo['_id'])
    if request.method == 'POST':
        vehiculos_collection.update_one(
            {'_id': ObjectId(pk)},
            {'$set': {
                'make': request.POST['make'],
                'model': request.POST['model'],
                'price': request.POST['price'],
                'color': request.POST['color'],
                'year': request.POST['year'],
                'status': request.POST['status'],
            }}
        )
        return redirect('vehiculo-list')
    return render(request, 'mongoapp/vehiculo_form.html', {'vehiculo': vehiculo})

def vehiculo_delete(request, pk):
    redirect_response = require_admin(request)
    if redirect_response:
        return redirect_response

    vehiculo = vehiculos_collection.find_one({'_id': ObjectId(pk)})
    vehiculo['id'] = str(vehiculo['_id'])
    if request.method == 'POST':
        vehiculos_collection.delete_one({'_id': ObjectId(pk)})
        return redirect('vehiculo-list')
    return render(request, 'mongoapp/vehiculo_confirm_delete.html', {'vehiculo': vehiculo})


def vehiculo_cliente(request):
    redirect_response = require_client(request)
    if redirect_response:
        return redirect_response

    vehiculos = list(vehiculos_collection.find())
    for v in vehiculos:
        v['id'] = str(v['_id'])

    disponibles = sum(1 for v in vehiculos if v.get('status') == 'disponible')
    vendidos = sum(1 for v in vehiculos if v.get('status') == 'vendido')

    return render(request, 'mongoapp/vehiculo_cliente.html', {
        'vehiculos': vehiculos,
        'disponibles': disponibles,
        'vendidos': vendidos,
        'role': request.session.get('role'),
        'user_name': request.session.get('user'),
    })