from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass
class BaseModel(models.Model):
    activate = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, null =True)
    updated_date = models.DateTimeField(auto_now=True, null =True)

    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=100, default=True)

    def __str__(self):
        return self.name

class Courses(BaseModel):
    subject = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ('subject','category')

class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='lesson/%Y/%m')
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.subject

class Tag(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return  self.name