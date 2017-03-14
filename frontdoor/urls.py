from django.conf.urls import url
from .views import FrontDoorNewsView

urlpatterns = [
    url(r'^', FrontDoorNewsView.as_view(), name='main-page'),
]
