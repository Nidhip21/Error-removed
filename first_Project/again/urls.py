from django.urls import path
from again import views


urlpatterns =[
    path('first/', views.index, name="index"),
    path('next/', views.nidhi, name="nidhi"),
    path('', views.template, name="template"),
    path('form/', views.form_view, name="forml")
]
