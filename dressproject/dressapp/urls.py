from django.contrib import admin
from django.urls import path, include

from . import views
app_name='dressapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('dress/<int:dress_id>/',views.detail,name='detail'),
    path('add/',views.add_dress,name='add_dress'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')

]