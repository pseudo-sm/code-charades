
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('fetch/', views.fetch,name="fetch"),
    path('code/',views.code,name="code"),
    path('compile/',views.compile,name="compile"),
    path('start-exam/',views.start_exam),
    path('compile/',views.compile,name="compile"),
    path('submit/',views.submit,name="submit"),
    path('editor/',views.editor,name="editor"),

]
