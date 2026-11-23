from django.contrib import admin
from courses.models import Category, Courses, Lesson, Tag
from django.utils.html import mark_safe
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'description']
    readonly_fields = ['avatar']
    def avatar(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'\
                    .format(url=obj.image.name)
)

admin.site.register(Category)
admin.site.register(Courses, CourseAdmin)

class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject','created_date', 'courses']
    list_filter = ['subject', 'created_date']
    search_fields = ['subject', 'course__subject']

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }

        js = ('/static/js/script.js',)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)

