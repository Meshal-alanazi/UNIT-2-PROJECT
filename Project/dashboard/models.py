from django.db import models

# Create your models here.
class Project(models.Model):
    class CategoryChoices(models.TextChoices):
        UNIVERSITY_PROJECT = "University project", "University project"
        DATA_SCIENCE = "Data Science", "Data Science"
        MACHINE_LEARNING = "Machine Learning", "Machine Learning"
        PHOTOGRAPHY = "Photography", "Photography"
        PERSONAL_PROJECTS = "Personal Projects", "Personal Projects"
        BOOTCAMP_PROJECTS = "Bootcamp Projects", "Bootcamp Projects"
        

     
    title = models.CharField(max_length=100)
    about = models.TextField()
    image = models.ImageField(upload_to="images/",default="images/1.jpg")
    category = models.CharField(max_length=50, choices=CategoryChoices.choices)
   