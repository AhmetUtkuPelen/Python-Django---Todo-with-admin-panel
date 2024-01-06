from django.urls import path
from .views import *

urlpatterns = [
    path('', todo_anasayfa, name="todo_anasayfa_page"),

    path('detail/<slug:todo_slug>/', todo_detail, name="todo_detail_page"),

    path('category/<slug:category_slug>/', todo_category, name="todo_category_page"),

    path('sub-category/<slug:sub_category_slug>/', todo_sub_category, name="todo_sub_category_page"),

    path('create/', todo_add, name="todo_add_page")

]
