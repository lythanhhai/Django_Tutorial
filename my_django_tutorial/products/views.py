from django.shortcuts import render, get_object_or_404, redirect
from products.form import ProductForm, ProductFormPure
from products.models import Product
from django.http import Http404
# Create your views here.

# def product_create_view(request, *arg, **kwarg):
#     form = ProductFormPure()
#     if request.method == "POST":
#         form = ProductFormPure(request.POST or None)
#         if form.is_valid():
#             # form.save()
#             print(form.cleaned_data)
#             Product.objects.create(title=form.cleaned_data['title'], description=form.cleaned_data['description'], price=form.cleaned_data['price'])

#     my_context = {
#         'form': form
#     }
#     return render(request, 'products/product_create.html', my_context)

# def product_create_view(request, *arg, **kwarg):
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#     my_context = {
#     }
#     return render(request, 'products/product_create.html', my_context)

def product_create_view(request, *arg, **kwarg):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    my_context = {
        'form': form
    }
    return render(request, 'products/product_create.html', my_context)

def product_detail_view(request, *arg, **kwarg):
    list = Product.objects.all()
    my_context = {
        # 'title': obj.title,
        # 'description': obj.description,
        # 'price': obj.price,
        # 'summary': obj.summary,
        'list': list
    }
    return render(request, 'products/product_detail.html', my_context)

def dynamic_url_view(request, id):
    obj = get_object_or_404(Product, id= id)
    try:
        obj = Product.objects.get(id= id)
    except Product.DoesNotExist:
        raise Http404

    context={
        'obj': obj
    }
    return render(request, 'products/product_detail_item.html', context)

def product_delete_view(request, id):
    # kiểm tra xem có sản phẩm tồn tại không
    obj = get_object_or_404(Product, id= id)
    # try:
    #     obj = Product.objects.get(id= id)
    # except Product.DoesNotExist:
    #     raise Http404
    if request.method == "POST":
        obj.delete()
        return redirect("../../")

    context = {
        'obj': obj
    }

    return render(request, 'products/product_delete.html', context)