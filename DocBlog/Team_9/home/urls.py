from django.urls import path

from Team_9.views import afficher
from Team_9.views import Hello

urlpatterns = [
    path('',afficher),
    path('hello/', Hello.as_view()),
]