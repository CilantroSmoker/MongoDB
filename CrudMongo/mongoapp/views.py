from django.shortcuts import render, redirect
from bson import ObjectId
from .models import vehiculos_collection

def vehiculo_list(request):
    vehiculos = list(vehiculos_collection.find())
    for v in vehiculos:
        v['id'] = str(v['_id'])
    return render(request, 'mongoapp/vehiculo_list.html', {'vehiculos': vehiculos})

def vehiculo_create(request):
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
    vehiculo = vehiculos_collection.find_one({'_id': ObjectId(pk)})
    vehiculo['id'] = str(vehiculo['_id'])
    if request.method == 'POST':
        vehiculos_collection.delete_one({'_id': ObjectId(pk)})
        return redirect('vehiculo-list')
    return render(request, 'mongoapp/vehiculo_confirm_delete.html', {'vehiculo': vehiculo})