from django.apps import AppConfig


class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todolist.bot'
    verbose_name = 'Телеграм Бот'