from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.

class choiceinline(admin.TabularInline):
	model=Choice
	extra=2

class QuestionAdmin(admin.ModelAdmin):
	fieldsets=[
		(None, {'fields': ['question_text']}),
		('Date information', {'fields':['pub_date'], 'classes': ['collapse'] })
	]
	inlines=[choiceinline]
	list_display=['question_text','pub_date','was_published_recently']
	list_filter=['pub_date']
	search_fields=['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)