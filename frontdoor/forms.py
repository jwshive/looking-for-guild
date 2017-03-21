from django import forms


class FeedbackForm(forms.Form):
    feedback_subject = forms.CharField()
    feedback_body = forms.CharField(widget=forms.Textarea)

