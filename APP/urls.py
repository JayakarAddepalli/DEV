from django.urls import path
from .views import *

app_name = 'APP'

urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('<str:category>/', CategoryBlogs.as_view(), name='category'),
    path('Python/<int:id>/', Info.as_view(), name='information'),
    path('HTML5/<int:id>/', HTMLInfo.as_view(), name='htmlInfo'),
    path('CSS3/<int:id>/', CSSInfo.as_view(), name='cssInfo')
]