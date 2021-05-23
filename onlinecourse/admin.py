from django.contrib import admin
# <HINT> Import any new Models here
from .models import Question, Choice, Submission,Enrollment
from .models import Course, Lesson, Instructor, Learner

# <HINT> Register QuestionInline and ChoiceInline classes here
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 20

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here
class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    question_display = ["question_text"]
    question_grade = ["grade"]

class ChoiceAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    choice_display = ["choice_text"]
    choice_correctness = ["is_correct"]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)

admin.site.register(Choice)
admin.site.register(Question)