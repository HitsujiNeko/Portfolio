from django.urls import path
from . import views
from .views import ContactView

app_name = "portfolio_app"

urlpatterns=[
    path("",views.index, name="index"), path('contact/', ContactView.as_view(), name='contact'),
]