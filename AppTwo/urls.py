from django.urls import path
from AppTwo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('access_records/', views.access_records, name='access-records'),
    path('help/', views.help_index, name='help-index'),
    path('users/', views.display_users, name='user-data'),
    path('form/', views.form_name_view, name='sample-form'),
    path('register/', views.register, name='register-user'),
    path('login/', views.user_login, name='user-login'),
]
