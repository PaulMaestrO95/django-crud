from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)










# def show_catalog(request):
#     template = 'catalog.html'
#     if 'sort' in request.GET:
#         sort_type = str(request.GET.get('sort'))
#         print(sort_type)
#         if sort_type == 'min_price':
#             sort_type = 'price'
#             context = {
#                 'phones': reversed(Phone.objects.order_by(sort_type))
#             }
#             return render(request, template, context)
#         if sort_type == 'max_price':
#             sort_type = 'price'
#             context = {
#                 'phones': reversed(Phone.objects.order_by(sort_type))
#             }
#             return render(request, template, context)
#         context = {
#             'phones': reversed(Phone.objects.order_by(sort_type))
#         }
#         return render(request, template, context)
#     context = {
#         'phones': Phone.objects.all()
#     }
#     return render(request, template, context)
#
#
# def show_product(request, slug):
#     template = 'product.html'
#     phone = Phone.objects.get(slug=slug)
#     context = {
#         'phone': phone
#     }
#     return render(request, template, context)


