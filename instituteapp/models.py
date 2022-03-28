from django.db import models


class CourseData(models.Model):
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=30)
    start_time = models.TimeField()
    start_date = models.DateField()
    duration = models.CharField(max_length=20)
    trainer_name = models.CharField(max_length=20)
    trainer_exep = models.IntegerField()




class FeedbackData(models.Model):
    name = models.CharField(max_length=20)
    rating = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True )
    feedback = models.CharField(max_length=100)

class ContactData(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    company = models.CharField(max_length=20)
    salary = models.IntegerField()
    location = models.CharField(max_length=15)

