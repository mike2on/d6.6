from django.urls import path
from .views import PostList, Event


urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>', Event.as_view()),
]
