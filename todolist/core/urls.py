from django.urls import path

from todolist.core.views import SignUpView, LoginView, UserView, UpdatePasswordView

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('user', UserView.as_view(), name='user'),
    path('update_password', UpdatePasswordView.as_view(), name='update_password'),
]
