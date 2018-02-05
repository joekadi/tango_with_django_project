from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'page': pages_list}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    about_context_dict = {'boldmessage': "Rango says here is the about page."}
    return render(request, 'rango/about.html', about_context_dict)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        page = Page.objects.filter(category=category)

        context_dict['pages'] = page
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None

    return render(request, 'rango/category.html', context_dict)
