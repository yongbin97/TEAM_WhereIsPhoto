from django.urls import path
from . import views

# 비번 초기화
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = "user"

urlpatterns = [
    path("", views.main, name="main"),
    path("my_lnf/", views.my_lnf, name="my_lnf"),
    path('read_my_lnf/<int:pk>', views.read_my_lnf, name="read_my_lnf"),
    path("my_review/", views.my_review, name="my_review"),
    path('read_my_review/<int:pk>', views.read_my_review, name="read_my_review"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="log_out"),
    path("signup/", views.signup, name="signup"),
    path("change_password/", views.change_password, name='change_password'),
    path('modify/', views.modify, name='modify'),

    path('delete/', views.delete, name='delete'),
    path('notice/', views.notice, name="notice"),
    path('readnotice/<int:pk>', views.read_notice, name="read_notice"),
    path('nav_notice/', views.nav_notice, name="nav_notice"),
]