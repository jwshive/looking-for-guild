from django.conf.urls import url
from .views import FrontDoorNewsView, FeedbackFormView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', FrontDoorNewsView.as_view(), name='main-page'),
    url(r'^feedback', login_required(FeedbackFormView.as_view()), name='feedback'),
]
