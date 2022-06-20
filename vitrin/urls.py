from django.urls import path, include

from . import views


app_name = 'vitrin'


user_group_permission_patterns = [
    # path('user/', views.create_user, name='create_user'),
    path('user/', views.CreateUserView.as_view(), name='create_user'),
    # path('group/', views.create_group, name='create_group'),
    path('group/', views.CreateGroupView.as_view(), name='create_group'),
    # path('permission/', views.create_permission, name='create_permission'),
    path('permission/', views.CreatePermissionView.as_view(), name='create_permission'),
    path('user/formset/', views.CreateUserFormset.as_view(), name='create_user_formset'),
]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', include(user_group_permission_patterns)),
]
