from django.urls import path
from . import views
from .views import PostDetailView

app_name = 'project3'

urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]