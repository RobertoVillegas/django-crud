from .forms import ProductoForm, MarcaForm, PresentacionForm
from .models import Marca, Presentacion, Producto
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string

# Create your views here.


def index(request):
    return render(request, 'index.html')


def producto(request):
    productos = Producto.objects.all()
    marcas = Marca.objects.all()
    presentaciones = Presentacion.objects.all()
    return render(request, 'producto.html', {
        'productos': productos,
        'marcas': marcas,
        'presentaciones': presentaciones})


def save_productos(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            productos = Producto.objects.all()
            data['producto'] = render_to_string(
                'producto_lista.html', {'productos': productos})
        else:
            data['form_is_valid'] = False

    context = {
        'form': form
    }
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


def productoCreate(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
    else:
        form = ProductoForm()
    return save_productos(request, form, 'productoCreate.html')


def productoDetails(request, id):
    context = {}
    context["data"] = Producto.objects.get(id=id)

    return render(request, "productoDetails.html", context)


def productoUpdate(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
    else:
        form = ProductoForm(instance=producto)

    return save_productos(request, form, 'productoUpdate.html')


def productoDelete(request, id):
    data = dict()
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        data['form_is_valid'] = True
        productos = Producto.objects.all()
        data['producto'] = render_to_string(
            'producto_lista.html', {'productos': productos})
    else:
        context = {'producto': producto}
        data['html_form'] = render_to_string(
            'productoDelete.html', context, request=request)

    return JsonResponse(data)


def catalogo(request):
    context = {}

    # form = MarcaForm()
    marcas = Marca.objects.all()
    presentaciones = Presentacion.objects.all()
    context = {
        # 'form': form,
        'marcas': marcas,
        'presentaciones': presentaciones,
    }

    return render(request, 'catalogo.html', context)


def save_marcas(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            marcas = Marca.objects.all()
            data['catalogo'] = render_to_string(
                'marca_lista.html', {'marcas': marcas})
        else:
            data['form_is_valid'] = False

    context = {
        'form': form
    }
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


def marcaCreate(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
    else:
        form = MarcaForm()
    return save_marcas(request, form, 'marcaCreate.html')


def marcaDetails(request, id):
    context = {}
    context["data"] = Marca.objects.get(id=id)

    return render(request, "marcaDetails.html", context)


def marcaUpdate(request, id):
    marca = get_object_or_404(Marca, id=id)

    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
    else:
        form = MarcaForm(instance=marca)

    return save_marcas(request, form, 'marcaUpdate.html')


def marcaDelete(request, id):
    data = dict()
    marca = get_object_or_404(Marca, id=id)
    if request.method == 'POST':
        marca.delete()
        data['form_is_valid'] = True
        marcas = Marca.objects.all()
        data['catalogo'] = render_to_string(
            'marca_lista.html', {'marcas': marcas})
    else:
        context = {'marca': marca}
        data['html_form'] = render_to_string(
            'marcaDelete.html', context, request=request)

    return JsonResponse(data)


def save_presentaciones(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            presentaciones = Presentacion.objects.all()
            data['catalogo'] = render_to_string(
                'presentacion_lista.html', {'presentaciones': presentaciones})
        else:
            data['form_is_valid'] = False

    context = {
        'form': form
    }
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


def presentacionCreate(request):
    if request.method == 'POST':
        form = PresentacionForm(request.POST)
    else:
        form = PresentacionForm()
    return save_presentaciones(request, form, 'presentacionCreate.html')


def presentacionDetails(request, id):
    context = {}
    context["data"] = Presentacion.objects.get(id=id)

    return render(request, "presentacionDetails.html", context)


def presentacionUpdate(request, id):
    presentacion = get_object_or_404(Presentacion, id=id)

    if request.method == 'POST':
        form = PresentacionForm(request.POST, instance=presentacion)
    else:
        form = PresentacionForm(instance=presentacion)

    return save_presentaciones(request, form, 'presentacionUpdate.html')


def presentacionDelete(request, id):
    data = dict()
    presentacion = get_object_or_404(Presentacion, id=id)
    if request.method == 'POST':
        presentacion.delete()
        data['form_is_valid'] = True
        presentaciones = Presentacion.objects.all()
        data['catalogo'] = render_to_string(
            'presentacion_lista.html', {'presentaciones': presentaciones})
    else:
        context = {'presentacion': presentacion}
        data['html_form'] = render_to_string(
            'presentacionDelete.html', context, request=request)

    return JsonResponse(data)
