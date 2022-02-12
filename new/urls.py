from django.urls import path
from .views import BlogList,BlogDetail,BlogCreate,BlogUp,BlogDelete

urlpatterns = [
    path('post/<int:pk>/delete',BlogDelete.as_view(),name='post_delete'),
    path('post/<int:pk>/edit',BlogUp.as_view(),name='post_edit'),
    path('post/new/',BlogCreate.as_view(),name='post_new'),
    path('',BlogList.as_view(),name='home'),
    path('post/<int:pk>/',BlogDetail.as_view(),name='post_detail')
]