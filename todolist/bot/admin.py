# Register your models here.
from django.contrib import admin

from todolist.bot.models import TgUser


class BotAdmin(admin.ModelAdmin):
    list_display = ("tg_chat_id", "tg_id", "user")
    search_fields = ("tg_chat_id", "tg_id", "user")


admin.site.register(TgUser, BotAdmin)
