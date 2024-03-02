from django.urls import path
from . import views
from .models import MyModel

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    # Другие маршруты вашего модуля...
]

def hello_view(request):
    objects = MyModel.objects.all()
    # Дальнейшая обработка полученных объектов
    ...