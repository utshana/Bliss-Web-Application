from django.urls import path,include
from home import views

urlpatterns = [
    path("", views.home,name='index'),
    path("product", views.product,name='product'),
    path("blog", views.blog,name='blog'),
    path("contact", views.contact,name='contact'),
    path("aboutUs", views.aboutUs,name='about'),
    path("login", views.login,name='login'),
    path("SignUp", views.signUp,name='SignUp'),
    path("register", views.register,name='register'),
    path("loginMember", views.loginMember,name='loginMember'),
]