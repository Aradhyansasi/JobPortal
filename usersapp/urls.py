from django.urls import path
from usersapp import views

urlpatterns =[
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('signout/', views.SignOutView, name='signout'),
]