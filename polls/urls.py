from django.urls import path

from . import views

urlpatterns = [
    path('osoba/<int:pk>/', views.osoba_detail, name='osoba_detail'),
    path('osoba/update/<int:pk>/', views.osoba_update_delete),
    path('osoba/delete/<int:pk>/', views.osoba_update_delete),
    path('osoby/', views.osoba_list, name='osoba_list'),
    path('stanowisko/<int:pk>/', views.stanowisko_detail, name='stanowisko_detail'),
    path('stanowiska/', views.stanowisko_list, name='stanowiska_list'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
