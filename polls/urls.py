from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('osoba/<int:pk>/', views.OsobaDetail.as_view(), name='osoba_detail'),
    path('osoby/', views.OsobaList.as_view(), name='osoba_list'),

    path('stanowisko/<int:pk>/', views.stanowisko_detail, name='stanowisko_detail'),
    path('stanowiska/', views.stanowisko_list, name='stanowiska_list'),
]
