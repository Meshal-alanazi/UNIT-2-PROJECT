from django.db import models

# Create your models here.
class Project(models.Model):
    class CategoryChoices(models.TextChoices):
        WEB_DEVELOPMENT = "Web Development", "Web Development"
        DATA_SCIENCE = "Data Science", "Data Science"
        MACHINE_LEARNING = "Machine Learning", "Machine Learning"
        PHOTOGRAPHY = "Photography", "Photography"
        PERSONAL_PROJECTS = "Personal Projects", "Personal Projects"
        BOOTCAMP_PROJECTS = "Bootcamp Projects", "Bootcamp Projects"

     
    title = models.CharField(max_length=100)
    about = models.TextField()
    image = models.ImageField(upload_to="images/",default="images/default_FdKeTks.jpg")
    category = models.CharField(max_length=50, choices=CategoryChoices.choices)
   