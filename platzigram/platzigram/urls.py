from django.contrib import admin
from django.urls import path
from platzigram import views

urlpatterns = [
    path('hello-world', views.hello_world),
    path('hi', views.hi)
    # path('admin/', admin.site.urls),
]
