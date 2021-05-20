from django.contrib import admin
from .models import Poll, Choice, Vote

# admin.site.register(Poll)
# admin.site.register(Choice)
# admin.site.register(Vote)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date')
    list_display_links = ('question',)
    inlines = [ChoiceInline,]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('poll', 'choice_text')


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('poll', 'voted_by', 'choice')
    list_display_links = ('poll',)
