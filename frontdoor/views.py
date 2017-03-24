from django.views.generic import ListView, CreateView
from .models import FrontDoorNews, Feedback


class FrontDoorNewsView(ListView):
    queryset = FrontDoorNews.objects.filter(news_published=True)
    model = FrontDoorNews
    template_name = 'frontdoor/index.html'
    ordering = ['-news_creation_date']


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
