from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.loggedin, name='windex'),
    path('search/<str:query>', views.search, name='search')
]
