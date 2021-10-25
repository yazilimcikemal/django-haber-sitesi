from django.urls import path
from django.urls.resolvers import URLPattern
from .views import SignupView

urlpatterns=[
    path('signup/',SignupView.as_view(),name='signup'),
    

]

