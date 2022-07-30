from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index,
         name='index'),
    path('user_registration',views.user_registration,
         name='user_registration'),
    path('login_request',views.login_request,
         name='login_request'),
    # path('user_deletion',views.user_deletion,
    #      name='user_deletion')
]
