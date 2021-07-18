from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedTabularInline, NestedModelAdmin
from .models import Poll, Question, Choice


# inlines

class ChoiceInline(NestedTabularInline):
	model = Choice


class QuestionInline(NestedStackedInline):
	model = Question
	inlines = [ChoiceInline]


# model admins

@admin.register(Poll)
class PollAdmin(NestedModelAdmin):
	model = Poll
	inlines = [QuestionInline]
	list_display = ["title", "description", "author", "pub_date"]
	list_filter = ["author", "pub_date"]
	search_fields = ["title", "description"]


@admin.register(Question)
class QuestionAdmin(NestedModelAdmin):
	model = Question
	inlines = [ChoiceInline]
	list_display = ["question_text", "poll"]
	list_filter = ["poll"]
	search_fields = ["question_text"]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
	model = Choice
	list_display = ["choice_text", "question", "votes"]
	list_filter = ["question", "votes"]
	search_fields = ["choice_text"]
