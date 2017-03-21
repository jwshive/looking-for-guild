from django import forms


class FeedbackForm(forms.Form):
    guild_name = forms.CharField(max_length=255)
    guild_realm = forms.ForeignKey(Realms)
    guild_faction = forms.ForeignKey(Factions)
    guild_managers = forms.ForeignKey(Group)
    guild_information = forms.CharField(widget=forms.Textarea)
    guild_battlenet_website = forms.URLField()
    guild_external_website = forms.URLField()
    guild_wow_progress_link = forms.URLField()
    guild_warcraft_logs_link = forms.URLField()
    guild_world_of_logs_link = forms.URLField()
    is_recruiting = forms.BooleanField()    