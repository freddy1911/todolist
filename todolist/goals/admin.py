from django.contrib import admin

from todolist.goals.models import GoalCategory, Goal, GoalComment


class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created", "updated")
    search_fields = ("title", "user")
    list_filter = ('is_deleted',)


admin.site.register(GoalCategory, GoalCategoryAdmin)
admin.site.register(Goal)
admin.site.register(GoalComment)
