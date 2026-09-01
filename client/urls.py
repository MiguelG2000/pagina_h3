from django.urls import path, include
from client.views import (
    main_page
)


urlpatterns = [
    path('',main_page,name='main_page'),
]
