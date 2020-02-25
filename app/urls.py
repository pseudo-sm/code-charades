
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('fetch/', views.fetch,name="fetch"),
    path('code/',views.code,name="code"),
    path('compile/',views.compile,name="compile"),
    path('editor/',views.editor,name="editor")

]
