from django.contrib import admin
from .models import Guilds, RecruitmentPosts


class GuildAdmin(admin.ModelAdmin):
    list_display = ('guild_name', 'guild_realm', 'guild_faction', 'guild_created_by', 'is_active')


class RecruitmentPostAdmin(admin.ModelAdmin):
    list_display = ('guild_name', 'guild_faction', 'recruitment_title', 'is_post_active')


admin.site.register(Guilds, GuildAdmin)
admin.site.register(RecruitmentPosts, RecruitmentPostAdmin)

