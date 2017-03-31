from django.shortcuts import render
from django.views.generic import CreateView
from .models import FrontDoorNews, Feedback, WebsiteAPISettings
from players.models import Characters
import random


def FrontDoorNewsView(request):
    character_filters = {'looking_for_guild': True, 'is_character_active': True}
    all_lfg_character_ids = Characters.objects.filter(**character_filters).values_list("id", flat=True)
    try:
        random_idx = random.choice(all_lfg_character_ids)
        player_spotlight = Characters.objects.get(id=random_idx)
    except IndexError:
        player_spotlight = False

    context = {
        'player_spotlight': player_spotlight,
        'news_blog': FrontDoorNews.objects.filter(news_published=True).order_by('-news_creation_date'),
        'website_settings': WebsiteAPISettings.objects.get(pk=1)
    }
    return render(request, 'frontdoor/index.html', context)


class FeedbackFormView(CreateView):
    model = Feedback
    template_name = 'frontdoor/feedback.html'
    fields = ['feedback_subject', 'feedback_body']
    success_url = '/'

    def form_valid(self, form):
        form.instance.feedback_submitted_by = self.request.user
        return super(FeedbackFormView, self).form_valid(form)


class SearchForPlayers():
    pass


class SearchForGuilds():
    pass
