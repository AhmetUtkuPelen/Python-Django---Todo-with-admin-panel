from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def todo_anasayfa(request):

    categories = Category.objects.all()
    sub_catogeries = SubCategory.objects.all()
    todos = ToDo.objects.all()

    return render(request, 'todo_anasayfa.html', {
        'categories': categories,
        'sub_catogeries': sub_catogeries,
        'todos': todos,
    })


def todo_category(request, category_slug):

    category = Category.objects.get(slug = category_slug)
    todos = ToDo.objects.filter(category__id = category.id)

    return render(request, 'todo_category.html', {
        'category': category,
        'todos': todos,
    })


def todo_sub_category(request, sub_category_slug):

    sub_category = SubCategory.objects.get(slug = sub_category_slug)
    todos = ToDo.objects.filter(sub_category__id = sub_category.id)

    
    return render(request, 'todo_sub_category.html', {
        'sub_category': sub_category,
        'todos': todos,
    })


def todo_detail(request, todo_slug):

    todo = ToDo.objects.get(slug = todo_slug)


    return render(request, 'todo_detail.html', {
        'todo': todo
    })


def todo_add(request):

    if request.method == 'POST':
        form = AddToDo(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('todo_anasayfa_page')
        else:
            form = AddToDo()
            return render(request, 'todo_add.html', {
                'form': form
            })


    form = AddToDo()
    return render(request, 'todo_add.html', {
        'form': form
    })