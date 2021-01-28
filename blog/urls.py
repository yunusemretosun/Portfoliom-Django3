from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs,name='Bloglar'),#name burda url in adi yerine geciyor.
    path('<int:blog_id>/', views.detail,name='blogdetay'),#eger ki path kisminda sayi varsa bunu blog_id ye ordan viewsteki detail fonknuna atiyor
]
