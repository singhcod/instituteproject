from django.contrib import admin
from.models import CourseData

class AdminCourseData(admin.ModelAdmin):
    list_display = ['course_id',
                    'course_name',
                    'start_time',
                    'start_date',
                    'duration',
                    'trainer_name',
                    'trainer_exep']


admin.site.register(CourseData,AdminCourseData)

