from django.urls import path
from .views import FolderView, ImageView, ImageDetailView

urlpatterns = [
    path('folders/', FolderView.as_view(), name='folder-list-create'),
    path('folders/<str:foldername>/images/', ImageView.as_view(), name='image-list-create'),
    path('folders/<str:foldername>/images/<int:id>/', ImageDetailView.as_view(), name='image-detail'),
]