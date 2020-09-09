from django.urls import path
from .views import home
from .views import Home


urlpatterns = [
    # path('', Home.as_view(), name='Home'),
    path('', home, name='home'),
]
