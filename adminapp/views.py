from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User
from mainapp.models import ProductCategory
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, UserAdminCreateProductForm

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
   
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
   
    context = {
        'users': User.objects.all(),
    }
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user)

    context = {'form': form, 'user': user}
    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_remove(request, user_id):
    user = User.objects.get(id=user_id)
    # user.delete()
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))

@user_passes_test(lambda u: u.is_superuser)
def admin_product_categories(request):
    context = {
        'product_categories': ProductCategory.objects.all(),
    }

    return render(request, 'adminapp/admin-product_categories-read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_product_categories_update(request, product_category_id):
    category = ProductCategory.objects.get(id=product_category_id)
    if request.method == 'POST':
        form = UserAdminCreateProductForm(data=request.POST, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_product_categories'))
    else:
        form = UserAdminCreateProductForm(instance=category)

    context = {'form': form, 'product_category': category}
    return render(request, 'adminapp/admin-product_categories-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_product_categories_create(request):
    if request.method == 'POST':
        form = UserAdminCreateProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_product_categories'))
        else:
            print(form.errors)
    else:
        form = UserAdminCreateProductForm()

    context = {'form': form}
    return render(request, 'adminapp/admin-product_categories-create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_product_categories_remove(request, product_category_id):
    category = ProductCategory.objects.get(id=product_category_id)
    category.delete()
    return HttpResponseRedirect(reverse('admin_staff:admin_product_categories'))

