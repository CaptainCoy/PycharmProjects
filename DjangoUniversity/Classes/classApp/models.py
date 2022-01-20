from django.db import models

# Create your models here.
class DjangoClasses (models.Model):
    Title = models.CharField(max_length=50, default="", blank=True, null=False)
    CourseNumber = models.IntegerField()
    InstructorName = models.CharField(max_length=50, default="", blank=True, null=False)
    Duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.Title
