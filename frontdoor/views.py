from django.views.generic import ListView
from .models import FrontDoorNews


class FrontDoorNewsView(ListView):
    queryset = FrontDoorNews.objects.filter(news_published=True)
    model = FrontDoorNews
    template_name = 'frontdoor/index.html'
    ordering = ['-news_creation_date']