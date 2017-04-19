from django.contrib import admin
from .models import Guilds, RecruitmentPosts, GuildManagers


class GuildAdmin(admin.ModelAdmin):
    list_display = ('guild_name', 'guild_realm', 'guild_faction', 'guild_created_by', 'is_active', 'is_recruiting')


class RecruitmentPostAdmin(admin.ModelAdmin):
    list_display = ('guild_name', 'recruitment_title', 'is_post_active')


admin.site.register(Guilds, GuildAdmin)
admin.site.register(RecruitmentPosts, RecruitmentPostAdmin)
admin.site.register(GuildManagers)

